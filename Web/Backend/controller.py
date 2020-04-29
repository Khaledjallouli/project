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
    # jason = json.loads("""{
    #     "SoccerGames":[
    #         {
    #             "odds-home": 3.5,
    #             "odds-draw": 3.3,
    #             "odds-away": 2.1,
    #             "home-wins": 1,
    #             "home-draws": 3,
    #             "home-losses": 6,
    #             "home-goals": 11,
    #             "home-opposition"-goals: 16,
    #             "home-shots": 137,
    #             "home-shots_on_target": 67,
    #             "home-opposition_shots": 117,
    #             "home-opposition_shots_on_target": 53,
    #             "away-wins": 8,
    #             "away-draws": 2,
    #             "away-losses": 0,
    #             "away-goals": 15,
    #             "away-opposition"-goals: 6,
    #             "away-shots": 161,
    #             "away-shots_on_target": 78,
    #             "away-opposition_shots": 72,
    #             "away-opposition_shots_on_target": 30
    #         }
    #     ]
    # }""")
    
    #load model
    # model = helpers.load_model("current")

    #TODO current demo output follows, has to be changed later
    jason["finalResult"] = 0 # 0 == draw, 1 == hometeam win, 2 == awayteam win

    return json.dumps(jason)
