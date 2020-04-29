import tensorflow as tf

# load_model(modelname): Load model <modelname>.h5 from ml/ folder
def load_model(modelname):
    print("START load model")

    # Recreate the exact same model, including weights and optimizer.
    model = tf.keras.models.load_model('ml/'+modelname+'.h5')
    
    print("END load model")
    return model


# write_to_txt(filename,content): Write <content> to file with <filename>
def write_to_txt(filename,content):
    f = open(filename,"w+") # open file with filename <filename>
    f.write(content) # write <content> in file
    f.close() # close file