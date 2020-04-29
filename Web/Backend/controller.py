import ml.helpers as helpers
import json


def predict_soccerGame():
    #TODO insert dynamic inputjson
    # currently inputjson is filled manually
    jason = json.loads("""{
        "SoccerGames":[
            {
                "homeTeam": "FC Bayern",
                "awayTeam": "Dortmund",
                "dateMatch": "20/02/20"
            }
        ]
    }""")
    
    #load model
    # model = helpers.load_model("current")

    #TODO current demo output follows, has to be changed later

    jason["finalResult"] = 0 # 0 == draw, 1 == hometeam win, 2 == awayteam win

    return json.dumps(jason)
