import tensorflow as tf
import pandas as pd
from sklearn import preprocessing

# load_model(modelname): Load model <modelname>.h5 from ml/ folder
def load_model(modelname):
    print("START load model")

    # Recreate the exact same model, including weights and optimizer.
    model = tf.keras.models.load_model('ml/'+modelname+'.h5')
    
    print("END load model")
    return model


# exec_model(model, data): Execute <model> with <data>
def exec_model(model, df):
    print("START exec model")

    # normalize
    column_names_to_not_normalize = ['result']
    column_names_to_normalize = [x for x in list(df) if x not in column_names_to_not_normalize ]
    x = df[column_names_to_normalize].values
    x_scaled = preprocessing.normalize(x)
    df[column_names_to_normalize] = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = df.index)   
    n = preprocessing.normalize(df[column_names_to_normalize])

    # predict
    result = model.predict(n, batch_size=1)

    print("END exec model")
    return result


def prepare_data(matches):

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

    return prepared_data
    # prepared_data == [own-wins, own-draws, own-losses, own-goals, opposition-goals, own-shots, own-shots-on-target, opposition-shots, opposition-shots-on-target]