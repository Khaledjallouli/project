import ml.helpers as ml
import db.helpers as db
import fetching.helpers as fetching
import json
import pandas as pd
import numpy
from sklearn import preprocessing


def predict_soccerGame():

    #TODO insert dynamic inputjson
    # first row of sliding02.csv
    #TODO: unify names ['_'|'-']
    jasonstring = '{"0":{"result": "H","odds-home": 3.5,"odds-draw": 3.3,"odds-away": 2.1,"home-wins": 1,"home-draws": 3,"home-losses": 6,"home-goals": 11,"home-opposition-goals": 16,"home-shots": 137,"home-shots_on_target": 67,"home_opposition_shots": 117,"home-opposition_shots_on_target": 53,"away-wins": 8,"away-draws": 2,"away-losses": 0,"away-goals": 15,"away-opposition-goals": 6,"away-shots": 161,"away-shots_on_target": 78,"away-opposition_shots": 72,"away-opposition_shots_on_target": 30}}'

    df = pd.read_json(jasonstring).T # read json and create dataframe
    
    model = ml.load_model("model02_H3_M") # load model

    predictedResultArray = ml.exec_model(model,df) # retrieve result from model

    predictedResult = numpy.argmax(predictedResultArray, axis=None) # get max value

    print(predictedResult)
    #jason["finalResult"] = 0 # 0 == draw, 1 == hometeam win, 2 == awayteam win

    #TODO insert correct homeTeam and awayTeam and dateMatch
    jason = json.loads("""{
        "SoccerGames":[
            {
                "homeTeam": "A Home-Team",
                "awayTeam": "An Away-Team",
                "dateMatch": "20/02/20"
            }
        ]
    }""")

    jason["SoccerGames"][0]["finalResult"] = int(str(predictedResult)) # not beautiful, but works for now

    return json.dumps(jason)


def fetchdata(file):
    for match in fetching.fetchdata("19-20"): # for each past match of season 2019-2020
        db.add_match(file,match[0],match[1],match[2],match[3],match[4],match[5],match[6],match[7],match[8],match[9],match[10],match[11],match[12])


def preparedata(file,hometeam,awayteam,date):

    dbmatch = db.get_match(file,hometeam,awayteam,date)
    
    home_prepared_data = ml.prepare_data(db.get_teamhistory(file,hometeam,date))
    away_prepared_data = ml.prepare_data(db.get_teamhistory(file,awayteam,date))
    # prepared_data == [home-wins, home-draws, home-losses, home-goals, home-opposition-goals, home-shots, home-shots-on-target, home-opposition-shots, home-opposition-shots-on-target]
    
    prepared_data = {
        "result": dbmatch[2],
        "odds-home": dbmatch[6],
        "odds-draw": dbmatch[7],
        "odds-away": dbmatch[8],
        "home-wins": home_prepared_data[0], # calculated
        "home-draws": home_prepared_data[1], # calculated
        "home-losses": home_prepared_data[2], # calculated
        "home-goals": home_prepared_data[3], # calculated
        "home-opposition-goals": home_prepared_data[4], # calculated
        "home-shots": home_prepared_data[5], # calculated
        "home-shots-on-target": home_prepared_data[6], # calculated
        "home-opposition-shots": home_prepared_data[7], # calculated
        "home-opposition-shots-on-target": home_prepared_data[8], # calculated
        "away-wins": away_prepared_data[0], # calculated
        "away-draws": away_prepared_data[1], # calculated
        "away-losses": away_prepared_data[2], # calculated
        "away-goals": away_prepared_data[3], # calculated
        "away-opposition-goals": away_prepared_data[4], # calculated
        "away-shots": away_prepared_data[5], # calculated
        "away-shots-on-target": away_prepared_data[6], # calculated
        "away-opposition-shots": away_prepared_data[7], # calculated
        "away-opposition-shots-on-target": away_prepared_data[8] # calculated
    }

    dic = {"0" : prepared_data}

    return json.dumps(dic)


# testing:
def main():
    file = "db/database.sqlite"
    db.create_database(file)
    fetchdata(file)
    jasonstring = preparedata(file,"sc-paderborn-07","borussia-dortmund",20200601)

    df = pd.read_json(jasonstring).T # read json and create dataframe
    model = ml.load_model("model02_H3_M") # load model
    predictedResultArray = ml.exec_model(model,df) # retrieve result from model
    predictedResult = numpy.argmax(predictedResultArray, axis=None) # get max value
    print(predictedResult)
    #jason["finalResult"] = 0 # 0 == draw, 1 == hometeam win, 2 == awayteam win
if __name__ == "__main__":
    main()