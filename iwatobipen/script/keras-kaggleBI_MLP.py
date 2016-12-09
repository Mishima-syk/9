from sklearn.cross_validation import train_test_split
from keras.utils.np_utils import to_categorical
import pandas as pd
import numpy as np

# prepare dataset
train = pd.read_csv( "./kaggle/train.csv", header=0 )
print( train.shape )

Y = train.Activity
X = train.ix[:,1:]
train_X, test_X, train_Y, test_Y = train_test_split( X, Y, test_size=0.3, random_state=123 )
train_X, test_X = np.asanyarray( train_X ), np.asanyarray( test_X )
train_Y, test_Y = np.asanyarray( train_Y ), np.asanyarray( test_Y )

print( train_X.shape )
print( train_Y.shape, set( train_Y ) )



from keras.models import Sequential
model = Sequential()
from keras.layers import Dense, Activation
model.add( Dense( output_dim=100, input_dim=1776 ) )
model.add( Activation( "relu" ) )
model.add( Dense( output_dim=2 ) )
model.add( Activation( "softmax" ) )
model.compile( optimizer="sgd",
               loss="categorical_crossentropy",
               metrics = ["accuracy"] )

hist = model.fit( train_X, to_categorical(train_Y), nb_epoch=20, batch_size=100 )

pred_Y = model.predict_classes( test_X )

from sklearn.metrics import confusion_matrix, classification_report
print( "CONFUSION MATRICS" )
print( confusion_matrix( test_Y, pred_Y ) )
print( "REPORT" )
print( classification_report( test_Y, pred_Y ))
