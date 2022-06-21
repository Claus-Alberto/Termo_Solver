import sqlite3

# con = sqlite3.connect('words.db')

# cur = con.cursor()

# cur.execute('CREATE TABLE words (word TEXT, meaning TEXT, size INTEGER)')

# con.commit()

# with open('words.txt') as f:
#     while True:
#         content = f.readline().replace('\n', '')
#         if not content: break
#         cur.execute(f"INSERT INTO words VALUES ('{content}','',{len(content)})")
        
# con.commit()

# con.close()

con = sqlite3.connect('words.db')

cur = con.cursor()

cur.execute('CREATE TABLE english_words (word TEXT, meaning TEXT, size INTEGER)')

con.commit()

with open('eng_words.txt') as f:
    while True:
        content = f.readline().replace('\n', '')
        if not content: break
        cur.execute(f"INSERT INTO english_words VALUES ('{content}','',{len(content)})")
        
con.commit()

con.close()