import numpy as np
import pandas as pd
import sys

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs

from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.wrappers.scikit_learn import KerasRegressor

def getFpArr( mols, nBits = 1024 ):
    fps = [ AllChem.GetMorganFingerprintAsBitVect( mol, 2, nBits=nBits ) for mol in mols ]
    X = []
    for fp in fps:
        arr = np.zeros( (1,) )
        DataStructs.ConvertToNumpyArray( fp, arr )
        X.append( arr )
    return X

def getResponse( mols, prop="ACTIVITY" ):
    Y = []
    for mol in mols:
        act = mol.GetProp( prop )
        act = 9. - np.log10( float( act ) )
        Y.append( act )
    return Y

def base_model():
    model = Sequential()
    model.add( Dense( input_dim=1024, output_dim = 200 ) )
    model.add( Activation( "relu" ) )
    model.add( Dense( 200 ) )
    model.add( Activation( "relu" ) )
    model.add( Dense( 1 ) )
    model.add( Activation( 'relu' ) )
    model.compile( loss="mean_squared_error",  optimizer="adam" )
    return model


if __name__ == '__main__':
    filename = sys.argv[1]
    sdf = [ mol for mol in Chem.SDMolSupplier( filename ) ]
    X = getFpArr( sdf )
    Y = getResponse( sdf )

    trainx, testx, trainy, testy = train_test_split( X, Y, test_size=0.2, random_state=0 )
    trainx, testx, trainy, testy = np.asarray( trainx ), np.asarray( testx ), np.asarray( trainy ), np.asarray( testy )
    estimator = KerasRegressor( build_fn = base_model,
                                nb_epoch=100,
                                batch_size=50,
                                 )
    estimator.fit( trainx, trainy )
    pred_y = estimator.predict( testx )
    r2 = r2_score( testy, pred_y )
    rmse = mean_squared_error( testy, pred_y )
    print( "KERAS: R2 : {0:f}, RMSE : {1:f}".format( r2, rmse ) )
