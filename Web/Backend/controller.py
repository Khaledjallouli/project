import ml.helpers as ml
import db.helpers as db
import fetching.helpers as fetching
import json
import pandas as pd
import numpy
from sklearn import preprocessing
from datetime import datetime
from os import path


dbfile = "db/database.sqlite"
season = "19-20"
classificationmodelname = "classification_model"
regressionmodelname= "regression_model"

def getSoccerMatchesClassification():
    result_object = {"SoccerGames": []}

    if path.exists(dbfile): # only if db-file exists
        for match in db.get_matches(dbfile): # for each unpredicted match
            date = datetime.strptime(str(match["date"]), "%Y%m%d") # get date from number
            formatted_date = datetime.strftime(date, "%d/%m/%Y") # string from date
            predicted_match = {
                "homeTeam": match["home-team"],
                "awayTeam": match["away-team"],
                "dateMatch": formatted_date,
                "predictedResult": match["predicted-classification-result"],
                "actualResult": str(match["home-goals"]) + ":" + str(match["away-goals"])
            }
            result_object["SoccerGames"].append(predicted_match)
    
    return json.dumps(result_object)


def getSoccerMatchesRegression():
    result_object = {"SoccerGames": []}

    if path.exists(dbfile): # only if db-file exists
        for match in db.get_matches(dbfile): # for each unpredicted match
            date = datetime.strptime(str(match["date"]), "%Y%m%d") # get date from number
            formatted_date = datetime.strftime(date, "%d/%m/%Y") # string from date
            predicted_match = {
                "homeTeam": match["home-team"],
                "awayTeam": match["away-team"],
                "dateMatch": formatted_date,
                "predictedResult": match["predicted-regression-result"],
                "actualResult": str(match["home-goals"]) + ":" + str(match["away-goals"])
            }
            result_object["SoccerGames"].append(predicted_match)
    
    return json.dumps(result_object)


def fetchNewMatches():
    db.create_database(dbfile) # create db if not exists

    classificationmodel = ml.load_model(classificationmodelname) # load model for classification
    regressionmodel = ml.load_model(regressionmodelname) # load model for regression

    for match in fetching.fetchseason(season): # for each past match of season 2019-2020
        hometeamdata = db.get_teamhistory(dbfile,match["home-team"],match["date"]) # get history
        awayteamdata = db.get_teamhistory(dbfile,match["away-team"],match["date"]) # get history
        prepared_data = ml.prepare_matchdata(match,hometeamdata,awayteamdata) # prepare data for model

        predictedClassificationResult = ml.exec_classification_model(classificationmodel,prepared_data) # run the model
        predictedRegressionResult = ml.exec_regression_model(regressionmodel,prepared_data) # run the model

        db.add_match(dbfile,match["home-team"],match["away-team"],match["date"],predictedClassificationResult,predictedRegressionResult,match["odds-home"],match["odds-draw"],match["odds-away"],match["home-goals"],match["home-shots"],match["home-shots-on-target"],match["away-goals"],match["away-shots"],match["away-shots-on-target"])
    return "ok"


def retrainClassification():
    matches = []
    for match in db.get_matches(dbfile): # for each match in db
        hometeamdata = db.get_teamhistory(dbfile,match["home-team"],match["date"]) # get history
        awayteamdata = db.get_teamhistory(dbfile,match["away-team"],match["date"]) # get history
        prepared_data = ml.prepare_classificationtrainingmatchdata(match,hometeamdata,awayteamdata) # prepare data for model

        matches.append(prepared_data)
    
    model = ml.retrain_classification_model(matches) # build&create model

    ml.save_model(model,classificationmodelname)# save model

    # repredict everything!
    for match in db.get_matches(dbfile):
        hometeamdata = db.get_teamhistory(dbfile,match["home-team"],match["date"]) # get history
        awayteamdata = db.get_teamhistory(dbfile,match["away-team"],match["date"]) # get history
        prepared_data = ml.prepare_matchdata(match,hometeamdata,awayteamdata) # prepare data for model

        predictedClassificationResult = ml.exec_classification_model(model,prepared_data) # run the model

        db.update_matchprediction_classification(dbfile,match["home-team"],match["away-team"],match["date"],predictedClassificationResult)

    return "ok"


def retrainRegression():
    matches = []
    for match in db.get_matches(dbfile): # for each match in db
        hometeamdata = db.get_teamhistory(dbfile,match["home-team"],match["date"]) # get history
        awayteamdata = db.get_teamhistory(dbfile,match["away-team"],match["date"]) # get history
        prepared_data = ml.prepare_regressiontrainingmatchdata(match,hometeamdata,awayteamdata) # prepare data for model

        matches.append(prepared_data)
    
    model = ml.retrain_regression_model(matches) # build&create model

    ml.save_model(model,regressionmodelname)# save model

    # repredict everything!
    for match in db.get_matches(dbfile):
        hometeamdata = db.get_teamhistory(dbfile,match["home-team"],match["date"]) # get history
        awayteamdata = db.get_teamhistory(dbfile,match["away-team"],match["date"]) # get history
        prepared_data = ml.prepare_matchdata(match,hometeamdata,awayteamdata) # prepare data for model

        predictedRegressionResult = ml.exec_regression_model(model,prepared_data) # run the model

        db.update_matchprediction_regression(dbfile,match["home-team"],match["away-team"],match["date"],predictedRegressionResult)

    return "ok"


def predict_match(classificationmodel,regressionmodel,match):
    hometeamdata = db.get_teamhistory(dbfile,match[4],match[2]) # get history
    awayteamdata = db.get_teamhistory(dbfile,match[5],match[2]) # get history
    prepared_data = ml.prepare_matchdata(match[2],hometeamdata,awayteamdata) # prepare data for model
    predictedClassificationResult = ml.exec_classification_model(classificationmodel,prepared_data) # run the model
    predictedRegressionResult = ml.exec_regression_model(regressionmodel,prepared_data) # run the model

    return predictedClassificationResult,predictedRegressionResult

# testing:
def main():
    db.create_database(dbfile)
    fetchNewMatches()
    dbmatch = db.get_match(dbfile,"sc-paderborn-07","borussia-dortmund",20200601)
    hometeamdata = db.get_teamhistory(dbfile,"sc-paderborn-07",20200601)
    awayteamdata = db.get_teamhistory(dbfile,"borussia-dortmund",20200601)
    jasonstring = ml.prepare_matchdata(dbmatch,hometeamdata,awayteamdata) # prepare data for model

    df = pd.read_json(jasonstring).T # read json and create dataframe
    model = ml.load_model("model02_H3_M") # load model
    predictedResultArray = ml.exec_classification_model(model,df) # retrieve result from model
    predictedResult = numpy.argmax(predictedResultArray, axis=None) # get max value
    print(predictedResult)
    #jason["finalResult"] = 0 # 0 == draw, 1 == hometeam win, 2 == awayteam win
if __name__ == "__main__":
    main()