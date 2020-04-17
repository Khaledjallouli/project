from flask import Flask
from flask import request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/soccerGames', methods=['GET'])
def soccerGamesOutput():
    if request.method == 'GET':
        return soccerGamesListJson()
    else:
        return 0
        
def soccerGamesListJson():
    return {
        "nbGames": 2,
        "SoccerGames":[
            {
            "idMatch": 1,
            "homeTeam": "FC Bayern",
            "awayTeam": "Dortmund",
            "dateMatch": "20/02/20",
            "finalResult": 0 # 0: Draw, 1: Win HomeTeam, 2: Win AwayTeam
            },
            {
            "idMatch": 2,
            "homeTeam": "FC Bayern",
            "awayTeam": "Dortmund",
            "dateMatch": "20/02/20",
            "finalResult": 1
            },
            {
            "idMatch": 2,
            "homeTeam": "FC Bayern",
            "awayTeam": "Dortmund",
            "dateMatch": "20/02/20",
            "finalResult": 2
            }
        ]
    }
