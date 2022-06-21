import sqlite3
from flask import Flask, render_template, request, jsonify, g, send_from_directory
import os

app = Flask(__name__)

DATABASE = 'words.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def useDB(method):
    result = None
    conn = get_db()
    cur = conn.cursor()
    try:
        result = method(cur)
    finally:
        cur.close()
        conn.close()
    return result

def solveSingleWord(data, table, cur):
    jsonResult = {
        'answer': []
    }

    ask = data['ask']
    query = f"SELECT word FROM {table} WHERE size = 5 AND word LIKE '{ask[0]['letters']}'"
    
    for contain in ask[1]["contains"]:
        query += f" AND word LIKE '%{contain}%'"
        
    for notContain in ask[2]["notcontains"]:
        query += f" AND word NOT LIKE '%{notContain}%'"
        
    queryResult = cur.execute(query)
    
    for row in queryResult:
        jsonResult['answer'].append(row[0])

    return jsonResult

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/favicon.ico')
        
@app.route("/")
@app.route("/termo")
def termo():
    return render_template('termo.html')

@app.route('/solve_termo', methods=['POST'])
def solveTermo():
    return useDB(lambda cur: solveSingleWord(request.json, 'words', cur))

@app.route("/wordle")
def wordle():
    return render_template('wordle.html')

@app.route('/solve_wordle', methods=['POST'])
def solveWordle():
    return useDB(lambda cur: solveSingleWord(request.json, 'english_words', cur))
    

app.run()
