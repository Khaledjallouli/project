import json
import tensorflow as tf
import pandas as pd
from sklearn import preprocessing
import numpy

# load_model(modelname): Load model <modelname>.h5 from ml/ folder
def load_model(modelname):
    # Recreate the exact same model, including weights and optimizer.
    model = tf.keras.models.load_model('ml/'+modelname+'.h5')
    return model


# exec_model(model, data): Execute <model> with <data>
def exec_model(model, prepared_data):

    #TODO: The following step is probably unnecessary, as the index could be passed right away from the beginning (no for-loop required). But implementation isn't trivial...
    final_prepared_object = {"0":prepared_data} # creating the (required) index
    jasonstring = json.dumps(final_prepared_object) # prepare data for model
    df = pd.read_json(jasonstring).T # read json and create dataframe

    # normalize
    column_names_to_not_normalize = ['result']
    column_names_to_normalize = [x for x in list(df) if x not in column_names_to_not_normalize ]
    x = df[column_names_to_normalize].values
    x_scaled = preprocessing.normalize(x)
    df[column_names_to_normalize] = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = df.index)   
    n = preprocessing.normalize(df[column_names_to_normalize])

    # predict
    predictedResultArray = model.predict(n, batch_size=1)

    #TODO bug check for the following line; does it work as intended?
    return int(str(numpy.argmax(predictedResultArray, axis=None))) # get max value as int (not beautiful, but works)


def prepare_matchdata(match,hometeamdata,awayteamdata):
    home_prepared_data = prepare_teamdata(hometeamdata)
    away_prepared_data = prepare_teamdata(awayteamdata)
    # prepared_data == [home-wins, home-draws, home-losses, home-goals, home-opposition-goals, home-shots, home-shots-on-target, home-opposition-shots, home-opposition-shots-on-target]

    prepared_data = {
        "result": "", # not relevant for prediction...
        "odds-home": match["odds-home"],
        "odds-draw": match["odds-draw"],
        "odds-away": match["odds-away"],
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


def prepare_teamdata(matches):

    prepared_data = [0,0,0,0,0,0,0,0,0] # see after 'return' line
    for match in matches:
        if match[0] > match[3]: # if ownteam has more goals than oppositeteam
            prepared_data[0] += match[0] # own-wins
        elif match[0] < match[3]: # if ownteam has less goals than oppositeteam
            prepared_data[2] += match[2] # own-losses
        else: # draw
            prepared_data[1] += match[1] # own-draws
        prepared_data[3] += match[0] # own-goals
        prepared_data[4] += match[3] # opposition-goals
        prepared_data[5] += match[1] # own-shots
        prepared_data[6] += match[2] # own-shots-on-target
        prepared_data[7] += match[4] # opposition-shots
        prepared_data[8] += match[5] # opposition-shots-on-target

    return prepared_data # -> [own-wins, own-draws, own-losses, own-goals, opposition-goals, own-shots, own-shots-on-target, opposition-shots, opposition-shots-on-target]