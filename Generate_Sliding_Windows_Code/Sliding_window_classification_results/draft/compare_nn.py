#GOOGLE COLAB
##################################
from google.colab import drive
drive.mount('/content/gdrive')

import os
os.chdir("/content/gdrive/My Drive/thu-soccer/project/jupyter")
!git pull
!pip install -q git+https://github.com/tensorflow/docs
!pip install tensorboardcolab

##################################


import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
pd.set_option('display.max_columns', 999)

from sklearn import preprocessing
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow_core.estimator import inputs
from tensorflow import feature_column
from tensorflow.keras import layers
from tensorflow.keras import regularizers
from tensorflow import keras
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model

import tensorflow_docs as tfdocs
import tensorflow_docs.modeling
import tensorflow_docs.plots

from  IPython import display
from matplotlib import pyplot as plt

import numpy as np
import math

import pathlib
import shutil
import tempfile


def normalize_and_encode(dataframe):
    column_names_to_not_normalize = ['result']
    column_names_to_normalize = [x for x in list(dataframe) if x not in column_names_to_not_normalize ]
    x = dataframe[column_names_to_normalize].values
    x_scaled = preprocessing.normalize(x)
    df_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = dataframe.index)
    dataframe[column_names_to_normalize] = df_temp

    le = preprocessing.LabelEncoder()
    le.fit([ "H", "A", "D"])
    dataframe.loc[:,['result']]=le.transform(dataframe['result'])
    
    return dataframe

def get_X_and_y(dataframe):
    X = dataframe.drop(columns=['result']).values
    y = dataframe[['result']].values
    return X,y

df01 = pd.read_csv('../data/sliding01.csv', sep=',', index_col=0)
df02 = pd.read_csv('../data/sliding02_shots.csv', sep=',', index_col=0)
df03 = pd.read_csv('../data/sliding03_shots_extra.csv', sep=',', index_col=0)
df04 = pd.read_csv('../data/sliding04_shots_and_possession.csv', sep=',', index_col=0)
df05 = pd.read_csv('../data/sliding05_shots_and_possession_extra.csv', sep=',', index_col=0)

n01 = normalize_and_encode(df01)
n02 = normalize_and_encode(df02)
n03 = normalize_and_encode(df03)
n04 = normalize_and_encode(df04)
n05 = normalize_and_encode(df05)

train01, test01 = train_test_split(n01, test_size=0.05)
print(len(train01), 'train examples')
print(len(test01), 'test examples')

train02, test02 = train_test_split(n02, test_size=0.05)
print(len(train02), 'train examples')
print(len(test02), 'test examples')

train03, test03 = train_test_split(n03, test_size=0.05)
print(len(train03), 'train examples')
print(len(test03), 'test examples')

train04, test04 = train_test_split(n04, test_size=0.05)
print(len(train04), 'train examples')
print(len(test04), 'test examples')

train05, test05 = train_test_split(n05, test_size=0.05)
print(len(train04), 'train examples')
print(len(test04), 'test examples')

train_X01,train_y01 = get_X_and_y(train01)
train_X02,train_y02 = get_X_and_y(train02)
train_X03,train_y03 = get_X_and_y(train03)
train_X04,train_y04 = get_X_and_y(train04)
train_X05,train_y05 = get_X_and_y(train05)

test_X01,test_y01 = get_X_and_y(test01)
test_X02,test_y02 = get_X_and_y(test02)
test_X03,test_y03 = get_X_and_y(test03)
test_X04,test_y04 = get_X_and_y(test04)
test_X05,test_y05 = get_X_and_y(test05)


#Many models train better if you gradually reduce the learning rate during training. Use optimizers.schedules to reduce the learning rate over time:
#The code sets a schedules.InverseTimeDecay to hyperbolically decrease the learning rate to 1/2 of the base rate at 1000 epochs, 1/3 at 2000 epochs and so on.

def get_lr_schedule(train, batch_size):
    lr_schedule = tf.keras.optimizers.schedules.InverseTimeDecay(
    0.001,
    decay_steps=(len(train)//batch_size)*1000,
    decay_rate=1,
    staircase=False)
    return lr_schedule

def get_optimizer(train, batch_size):
    return tf.keras.optimizers.Adam(get_lr_schedule(train, batch_size))


#Each model in this tutorial will use the same training configuration. So set these up in a reusable way, starting with the list of callbacks.
#The training for this tutorial runs for many short epochs. To reduce the logging noise use the tfdocs.EpochDots which simply a . for each epoch and, and a full set of metrics every 100 epochs.

def get_callbacks(name):
    return [
        tfdocs.modeling.EpochDots(),
        tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=200),
        tf.keras.callbacks.TensorBoard(logdir/name),
      ]

def compile_and_fit(model, name, X, y, validation_split, batch_size, optimizer=None, max_epochs=EPOCHS):
    if optimizer is None:
        optimizer = get_optimizer(X, batch_size)
    model.compile(optimizer=optimizer,
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.summary()
     
    history = model.fit(
        X,
        y,
        validation_split=validation_split,
        batch_size=batch_size,
#        steps_per_epoch = 50, # (len(train_X01)//batch_size,
        epochs=max_epochs,
        callbacks=get_callbacks(name),
        verbose=0)
    
    model.save("../model/%s.h5" %name) 
    return history


def plot_history(model_history):
	plt.plot(model_history.history['accuracy'])
	plt.plot(model_history.history['val_accuracy'])
	plt.title("%s accuracy" %model_history)
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(['train', 'val'], loc='upper left')
	plt.show()
	
	plt.plot(model_history.history['loss'])
	plt.plot(model_history.history['val_loss'])
	plt.title("%s loss" %model_history)
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'val'], loc='upper left')
	plt.show()


#######################

BATCH_SIZE = 128*8
EPOCHS=10000
validation_split = 0.2
size_histories = {}


model01 = tf.keras.Sequential([
  layers.Dense(13, activation='relu',input_shape=(train_X01.shape[1],)), # 13 features
  layers.Dense(16, activation='relu'),
  layers.Dense(8, activation='relu'),
  layers.Dense(3, activation='softmax')
])


model02 = tf.keras.Sequential([
  layers.Dense(21, activation='relu',input_shape=(train_X02.shape[1],)), # 21 features
  layers.Dense(64, activation='relu'),
  layers.Dense(32, activation='relu'),
  layers.Dense(16, activation='relu'),
  layers.Dense(8, activation='relu'),
  layers.Dense(3, activation='softmax')
])

model03 = tf.keras.Sequential([
  layers.Dense(29, activation='relu',input_shape=(train_X03.shape[1],)), # 29 features
  layers.Dense(64, activation='relu'),
  layers.Dense(32, activation='relu'),
  layers.Dense(16, activation='relu'),
  layers.Dense(8, activation='relu'),
  layers.Dense(3, activation='softmax')
])

model04 = tf.keras.Sequential([
  layers.Dense(25, activation='relu',input_shape=(train_X04.shape[1],)), # 25 features
  layers.Dense(64, activation='relu'),
  layers.Dense(32, activation='relu'),
  layers.Dense(16, activation='relu'),
  layers.Dense(8, activation='relu'),
  layers.Dense(3, activation='softmax')
])

model05 = tf.keras.Sequential([
  layers.Dense(33, activation='relu',input_shape=(train_X05.shape[1],)), # 33 features
  layers.Dense(64, activation='relu'),
  layers.Dense(32, activation='relu'),
  layers.Dense(16, activation='relu'),
  layers.Dense(8, activation='relu'),
  layers.Dense(3, activation='softmax')
])


size_histories['model01'] = compile_and_fit(model01, 'model01', train_X01, train_y01, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
size_histories['model02'] = compile_and_fit(model02, 'model02', train_X02, train_y02, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
size_histories['model03'] = compile_and_fit(model03, 'model03', train_X03, train_y03, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
size_histories['model04'] = compile_and_fit(model04, 'model04', train_X04, train_y04, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
size_histories['model05'] = compile_and_fit(model05, 'model05', train_X05, train_y05, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)


plotter = tfdocs.plots.HistoryPlotter(metric = 'loss', smoothing_std=10)
plotter.plot(size_histories)


score = load_model('../model/model01.h5').evaluate(test_X01, test_y01, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/model02.h5').evaluate(test_X02, test_y02, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/model03.h5').evaluate(test_X03, test_y03, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/model04.h5').evaluate(test_X04, test_y04, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/model05.h5').evaluate(test_X05, test_y05, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")


# add Add weight regularization: L2

l2_model01 = tf.keras.Sequential([
  layers.Dense(13, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X01.shape[1],)), # 13 features
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(3, activation='softmax')
])


l2_model02 = tf.keras.Sequential([
  layers.Dense(21, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X02.shape[1],)), # 21 features
  layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(32, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(3, activation='softmax')
])

l2_model03 = tf.keras.Sequential([
  layers.Dense(29, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X03.shape[1],)), # 29 features
  layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(32, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(3, activation='softmax')
])

l2_model04 = tf.keras.Sequential([
  layers.Dense(25, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X04.shape[1],)), # 25 features
  layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(32, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(3, activation='softmax')
])

l2_model05 = tf.keras.Sequential([
  layers.Dense(33, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X05.shape[1],)), # 33 features
  layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(32, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dense(3, activation='softmax')
])

l2_histories = {}

l2_histories['l2_model01'] = compile_and_fit(model01, 'l2_model01', train_X01, train_y01, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
l2_histories['l2_model02'] = compile_and_fit(model02, 'l2_model02', train_X02, train_y02, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
l2_histories['l2_model03'] = compile_and_fit(model03, 'l2_model03', train_X03, train_y03, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
l2_histories['l2_model04'] = compile_and_fit(model04, 'l2_model04', train_X04, train_y04, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
l2_histories['l2_model05'] = compile_and_fit(model05, 'l2_model05', train_X05, train_y05, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)


plotter = tfdocs.plots.HistoryPlotter(metric = 'loss', smoothing_std=10)
plotter.plot(l2_histories)

plotter.plot(l2_histories)
a = plt.xscale('log')
plt.xlim([5, max(plt.xlim())])
#plt.ylim([0.5, 0.7])
plt.xlabel("Epochs [Log Scale]")

plot_history(l2_histories['l2_model01'])
plot_history(l2_histories['l2_model02'])
plot_history(l2_histories['l2_model03'])
plot_history(l2_histories['l2_model04'])
plot_history(l2_histories['l2_model05'])

score = load_model('../model/l2_model01.h5').evaluate(test_X01, test_y01, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/l2_model02.h5').evaluate(test_X02, test_y02, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/l2_model03.h5').evaluate(test_X03, test_y03, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/l2_model04.h5').evaluate(test_X04, test_y04, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/l2_model05.h5').evaluate(test_X05, test_y05, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

#Add dropout

drop_model01 = tf.keras.Sequential([
  layers.Dense(13, activation='relu',input_shape=(train_X01.shape[1],)), # 13 features
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])


drop_model02 = tf.keras.Sequential([
  layers.Dense(21, activation='relu',input_shape=(train_X02.shape[1],)), # 21 features
  layers.Dropout(0.2),
  layers.Dense(64, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(32, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])

drop_model03 = tf.keras.Sequential([
  layers.Dense(29, activation='relu',input_shape=(train_X03.shape[1],)), # 29 features
  layers.Dropout(0.2), 
  layers.Dense(64, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(32, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])

drop_model04 = tf.keras.Sequential([
  layers.Dense(25, activation='relu',input_shape=(train_X04.shape[1],)), # 25 features
  layers.Dropout(0.2),
  layers.Dense(64, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(32, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])

drop_model05 = tf.keras.Sequential([
  layers.Dense(33, activation='relu',input_shape=(train_X05.shape[1],)), # 33 features
  layers.Dropout(0.2),
  layers.Dense(64, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(32, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu'),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])

drop_histories = {}

drop_histories['drop_model01'] = compile_and_fit(drop_model01, 'drop_model01', train_X01, train_y01, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
drop_histories['drop_model02'] = compile_and_fit(drop_model02, 'drop_model02', train_X02, train_y02, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
drop_histories['drop_model03'] = compile_and_fit(drop_model03, 'drop_model03', train_X03, train_y03, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
drop_histories['drop_model04'] = compile_and_fit(drop_model04, 'drop_model04', train_X04, train_y04, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
drop_histories['drop_model05'] = compile_and_fit(drop_model05, 'drop_model05', train_X05, train_y05, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)

plotter = tfdocs.plots.HistoryPlotter(metric = 'loss', smoothing_std=10)
plotter.plot(drop_histories)

plotter.plot(drop_histories)
a = plt.xscale('log')
plt.xlim([5, max(plt.xlim())])
#plt.ylim([0.5, 0.7])
plt.xlabel("Epochs [Log Scale]")

plot_history(drop_histories['drop_model01'])
plot_history(drop_histories['drop_model02'])
plot_history(drop_histories['drop_model03'])
plot_history(drop_histories['drop_model04'])
plot_history(drop_histories['drop_model05'])

score = load_model('../model/drop_model01.h5').evaluate(test_X01, test_y01, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/drop_model02.h5').evaluate(test_X02, test_y02, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/drop_model03.h5').evaluate(test_X03, test_y03, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/drop_model04.h5').evaluate(test_X04, test_y04, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/drop_model05.h5').evaluate(test_X05, test_y05, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

# dropout and regularization

l2_drop_model01 = tf.keras.Sequential([
  layers.Dense(13, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X01.shape[1],)), # 13 features
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])


l2_drop_model02 = tf.keras.Sequential([
  layers.Dense(21, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X02.shape[1],)), # 21 features
  layers.Dropout(0.2),
  layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(32, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])

l2_drop_model03 = tf.keras.Sequential([
  layers.Dense(29, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X03.shape[1],)), # 29 features
  layers.Dropout(0.2), 
  layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(32, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])

l2_drop_model04 = tf.keras.Sequential([
  layers.Dense(25, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X04.shape[1],)), # 25 features
  layers.Dropout(0.2),
  layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(32, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])

l2_drop_model05 = tf.keras.Sequential([
  layers.Dense(33, activation='relu',kernel_regularizer=regularizers.l2(0.001),input_shape=(train_X05.shape[1],)), # 33 features
  layers.Dropout(0.2),
  layers.Dense(64, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(32, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(8, activation='relu',kernel_regularizer=regularizers.l2(0.001),),
  layers.Dropout(0.2),
  layers.Dense(3, activation='softmax')
])

l2_drop_histories = {}

l2_drop_histories['l2_drop_model01'] = compile_and_fit(l2_drop_model01, 'l2_drop_model01', train_X01, train_y01, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
l2_drop_histories['l2_drop_model02'] = compile_and_fit(l2_drop_model02, 'l2_drop_model02', train_X02, train_y02, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
l2_drop_histories['l2_drop_model03'] = compile_and_fit(l2_drop_model03, 'l2_drop_model03', train_X03, train_y03, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
l2_drop_histories['l2_drop_model04'] = compile_and_fit(l2_drop_model04, 'l2_drop_model04', train_X04, train_y04, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)
l2_drop_histories['l2_drop_model05'] = compile_and_fit(l2_drop_model05, 'l2_drop_model05', train_X05, train_y05, validation_split=validation_split,batch_size=BATCH_SIZE,max_epochs=EPOCHS)

plotter = tfdocs.plots.HistoryPlotter(metric = 'loss', smoothing_std=10)
plotter.plot(l2_drop_histories)

plot_history(l2_drop_histories['l2_drop_model01'])
plot_history(l2_drop_histories['l2_drop_model02'])
plot_history(l2_drop_histories['l2_drop_model03'])
plot_history(l2_drop_histories['l2_drop_model04'])
plot_history(l2_drop_histories['l2_drop_model05'])


score = load_model('../model/l2_drop_model01.h5').evaluate(test_X01, test_y01, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/l2_drop_model02.h5').evaluate(test_X02, test_y02, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/l2_drop_model03.h5').evaluate(test_X03, test_y03, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/l2_drop_model04.h5').evaluate(test_X04, test_y04, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")

score = load_model('../model/l2_drop_model05.h5').evaluate(test_X05, test_y05, verbose=3)
print("Test Score:", score[0])
print("Test Accuracy:", score[1])
print("#####")
