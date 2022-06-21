function solveTermo() {
    let l1 = document.getElementById('termo1').value == '' ? '_' : document.getElementById('termo1').value
    let l2 = document.getElementById('termo2').value == '' ? '_' : document.getElementById('termo2').value
    let l3 = document.getElementById('termo3').value == '' ? '_' : document.getElementById('termo3').value
    let l4 = document.getElementById('termo4').value == '' ? '_' : document.getElementById('termo4').value
    let l5 = document.getElementById('termo5').value == '' ? '_' : document.getElementById('termo5').value
    var settings = {
        "url": "solve_termo",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "ask": [
                {
                    "letters": l1+l2+l3+l4+l5
                },
                {
                    "contains": document.getElementById('termoContains').value
                },
                {
                    "notcontains": document.getElementById('termoNotContains').value
                }
            ]
        }),
    };
      
    let counter = 0
      
    $.ajax(settings).done(function (response) {
        document.getElementById('termoResults').innerHTML = ''
        response['answer'].every(v => {
            console.log(v);
            document.getElementById('termoResults').insertAdjacentHTML(
                'beforeend',
                `<p>` + v + `</p>`
            )
            counter++
            return true
        });
    });
    counter = 0
}

function solveWordle() {
    let l1 = document.getElementById('wordle1').value == '' ? '_' : document.getElementById('wordle1').value
    let l2 = document.getElementById('wordle2').value == '' ? '_' : document.getElementById('wordle2').value
    let l3 = document.getElementById('wordle3').value == '' ? '_' : document.getElementById('wordle3').value
    let l4 = document.getElementById('wordle4').value == '' ? '_' : document.getElementById('wordle4').value
    let l5 = document.getElementById('wordle5').value == '' ? '_' : document.getElementById('wordle5').value

    var settings = {
        "url": "solve_wordle",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "ask": [
                {
                    "letters": l1+l2+l3+l4+l5
                },
                {
                    "contains": document.getElementById('wordleContains').value
                },
                {
                    "notcontains": document.getElementById('wordleNotContains').value
                }
            ]
        }),
    };
      
    let counter = 0
      
    $.ajax(settings).done(function (response) {
        document.getElementById('wordleResults').innerHTML = ''
        response['answer'].every(v => {
            console.log(v);
            document.getElementById('wordleResults').insertAdjacentHTML(
                'beforeend',
                `<p>` + v + `</p>`
            )
            counter++
            return true
        });
    });
    counter = 0
}