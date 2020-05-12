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
    return(result)


# write_to_txt(filename,content): Write <content> to file with <filename>
def write_to_txt(filename,content):
    f = open(filename,"w+") # open file with filename <filename>
    f.write(content) # write <content> in file
    f.close() # close file