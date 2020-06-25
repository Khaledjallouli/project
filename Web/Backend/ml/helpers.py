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

# save_model(model,modelname): Save model <modelname>.h5 to ml/ folder
def save_model(model,modelname):
    model.save('ml/'+modelname+'.h5')

# exec_model(model, data): Execute <model> with <data>
def exec_classification_model(model, prepared_data):

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
    predictedresult = int(str(numpy.argmax(predictedResultArray, axis=None)))

    decoded_result = "D"
    if predictedresult == 1:
        decoded_result="H"
    elif predictedresult == 2:
        decoded_result="A"

    #TODO bug check for the following line; does it work as intended?
    return decoded_result # get max value as int (not beautiful, but works)

def retrain_classification_model(prepared_data):

    # create dataframe
    #TODO: The following step is probably unnecessary, as the index could be passed right away from the beginning (no for-loop required). But implementation isn't trivial...
    index = 0
    final_prepared_object = {}
    for match in prepared_data:
        final_prepared_object[str(index)] = match
        index = index+1
    jasonstring = json.dumps(final_prepared_object) # prepare data for model
    df = pd.read_json(jasonstring).T # read json and create dataframe

    # normalize
    column_names_to_not_normalize = ['result']
    column_names_to_normalize = [x for x in list(df) if x not in column_names_to_not_normalize ]
    x = df[column_names_to_normalize].values
    x_scaled = preprocessing.normalize(x)
    df[column_names_to_normalize] = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = df.index)   
    #n = preprocessing.normalize(df[column_names_to_normalize])
    le = preprocessing.LabelEncoder()
    le.fit([ "H", "D", "A"])
    df.loc[:,['result']]=le.transform(df['result'])

    # get X,y
    train_X = df.drop(columns=['result']).values
    train_y = df[['result']].values

    # build model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(35, activation='relu',input_shape=(train_X.shape[1],)), # 21 features
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='softmax')
    ])
    optimizer = tf.keras.optimizers.SGD(lr=0.01, momentum=0.9)
    model.compile(optimizer=optimizer,
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    # train model
    EPOCHS = 10000
    model.fit(
        train_X, train_y,
        epochs=EPOCHS, validation_split = 0.2, verbose=0, batch_size=128*8)
    return model

# exec_model(model, data): Execute <model> with <data>
def exec_regression_model(model, prepared_data):

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

    # decode
    home_prediction = decode(round_regression_result(predictedResultArray[:,0]))
    away_prediction = decode(round_regression_result(predictedResultArray[:,1]))

    return str(home_prediction) + ":" + str(away_prediction) # return as str (not beautiful, but works)

def retrain_regression_model(prepared_data):

    # create dataframe
    #TODO: The following step is probably unnecessary, as the index could be passed right away from the beginning (no for-loop required). But implementation isn't trivial...
    index = 0
    final_prepared_object = {}
    for match in prepared_data:
        final_prepared_object[str(index)] = match
        index = index+1
    jasonstring = json.dumps(final_prepared_object) # prepare data for model
    df = pd.read_json(jasonstring).T # read json and create dataframe

    # normalize
    column_names_to_not_normalize = ['result']
    column_names_to_normalize = [x for x in list(df) if x not in column_names_to_not_normalize ]
    x = df[column_names_to_normalize].values
    x_scaled = preprocessing.normalize(x)
    df[column_names_to_normalize] = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = df.index)   
    #n = preprocessing.normalize(df[column_names_to_normalize])

    # get X,y
    train_X = df.drop(columns=['home_team_goal','away_team_goal']).values
    train_y = df[['home_team_goal','away_team_goal']].values

    # build model
    model= tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(units=21, activation='relu', input_shape=(train_X.shape[1],)))
    model.add(tf.keras.layers.Dense(units=10, activation='relu'))
    model.add(tf.keras.layers.Dense(units=5, activation='relu'))
    model.add(tf.keras.layers.Dense(units=2))
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss='mse',
                    optimizer=optimizer,
                    metrics=['mae', 'mse','accuracy'])

    # train model
    EPOCHS = 1000
    model.fit(
        train_X, train_y,
        epochs=EPOCHS, validation_split = 0.2, verbose=0, batch_size=32)
    return model

def round_regression_result(val):
    if val <=1 and val > 0.67:
        return 1
    elif val <=0.67 and val >0.33:
        return 0.60
    elif val <= 0.33 and val > 0:
        return 0.20
    elif val <= 0 and val > -0.33:
        return -0.20
    elif val<=-0.33 and val> -0.67:
        return -0.60
    else:
        return -1

def encode(i):
    switcher = {
        0: -1,
        1: -0.6,
        2: -0.2,
        3: 0.2,
        4: 0.6,
        5: 1,
    }
    # 1 be assigned as default value of passed argument (if goals > 5)
    return switcher.get(i, 1)

def decode(i):
    switcher = {
        -1: 0,
        -0.6: 1,
        -0.2: 2,
        0.2: 3,
        0.6: 4,
        1: 5,
    }
    return switcher.get(i, "ERROR! Use Encode Before!")

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

def prepare_matchdata(match,hometeamdata,awayteamdata):
    home_prepared_data = prepare_teamdata(hometeamdata)
    away_prepared_data = prepare_teamdata(awayteamdata)
    # prepared_data == [home-wins, home-draws, home-losses, home-goals, home-opposition-goals, home-shots, home-shots-on-target, home-opposition-shots, home-opposition-shots-on-target]

    prepared_data = {
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

def prepare_classificationtrainingmatchdata(match,hometeamdata,awayteamdata):
    home_prepared_data = prepare_teamdata(hometeamdata)
    away_prepared_data = prepare_teamdata(awayteamdata)
    # prepared_data == [home-wins, home-draws, home-losses, home-goals, home-opposition-goals, home-shots, home-shots-on-target, home-opposition-shots, home-opposition-shots-on-target]

    result = "D"
    if match["home-goals"] > match["away-goals"]:
        result="H"
    elif match["away-goals"] > match["home-goals"]:
        result="A"

    prepared_data = {
        "result": result,
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

def prepare_regressiontrainingmatchdata(match,hometeamdata,awayteamdata):
    home_prepared_data = prepare_teamdata(hometeamdata)
    away_prepared_data = prepare_teamdata(awayteamdata)
    # prepared_data == [home-wins, home-draws, home-losses, home-goals, home-opposition-goals, home-shots, home-shots-on-target, home-opposition-shots, home-opposition-shots-on-target]

    prepared_data = {
        "home_team_goal": match["home-goals"],
        "away_team_goal": match["away-goals"],
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
