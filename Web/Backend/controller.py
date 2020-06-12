import ml.helpers as ml
import db.helpers as db
import fetching.helpers as fetching
import json
import pandas as pd
import numpy
from sklearn import preprocessing
from datetime import datetime

def predict_soccerGames():

    file = "db/database.sqlite"
    db.create_database(file)
    #fetching.fetchdata("19-20")
    fetchdata(file)
    model = ml.load_model("model02_H3_M") # load model
    result_object = {"SoccerGames": []}

    for match in db.get_matches(file): # for each unpredicted match
        prepared_data = preparedata(file,match[3],match[4],match[5]) # prepare data for model
        #TODO: The following step is probably unnecessary, as the index could be passed right away from the beginning (no for-loop required).
        final_prepared_object = {"0":prepared_data} # creating the (required) index
        jasonstring = json.dumps(final_prepared_object) # prepare data for model
        df = pd.read_json(jasonstring).T # read json and create dataframe
        predictedResultArray = ml.exec_model(model,df) # retrieve result from model
        predictedResult = numpy.argmax(predictedResultArray, axis=None) # get max value

        date = datetime.strptime(str(match[5]), "%Y%m%d") # get date from number
        formatted_date = datetime.strftime(date, "%d/%m/%Y") # string from date
        predicted_match = {
            "homeTeam": match[3],
            "awayTeam": match[4],
            "dateMatch": formatted_date,
            "finalResult": int(str(predictedResult)) # not beautiful, but works for now
        }
        result_object["SoccerGames"].append(predicted_match)
    
    return json.dumps(result_object)


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

    return prepared_data


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