import tensorflow as tf
import pandas

# load_model(modelname): Load model <modelname>.h5 from ml/ folder
def load_model(modelname):
    print("START load model")

    # Recreate the exact same model, including weights and optimizer.
    model = tf.keras.models.load_model('ml/'+modelname+'.h5')
    
    print("END load model")
    return model


# exec_model(model, data): Execute <model> with <data>
def exec_model(model, data):
    print("START exec model")

    # format input
    dataset = pandas.json_normalize(data)

    # predict
    result = model.predict(dataset, batch_size=1)

    print("END exec model")
    return(result)


# write_to_txt(filename,content): Write <content> to file with <filename>
def write_to_txt(filename,content):
    f = open(filename,"w+") # open file with filename <filename>
    f.write(content) # write <content> in file
    f.close() # close file