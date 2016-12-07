from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
import numpy as np
import tensorflow as tf
from sklearn import cross_validation
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from math import sqrt


def sdf2fp(filename):
    fps = []
    np_fps = []
    acts = []
    suppl = Chem.SDMolSupplier(filename)
    for mol in suppl:
        fps.append(AllChem.GetMorganFingerprintAsBitVect(mol, 2))
        acts.append(float(mol.GetProp("ACTIVITY")))
    for fp in fps:
        arr = np.zeros((1,))
        DataStructs.ConvertToNumpyArray(fp, arr)
        np_fps.append(arr)
    return np.array(np_fps), np.array(acts)


def dnn(x_train, x_test, y_train, y_test, steps=5000, hidden=[20, 20]):
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=x_train.shape[1])]
    tfl = tf.contrib.learn.DNNRegressor(hidden_units=hidden,
                                        feature_columns=feature_columns,
                                        model_dir=".az_model")

    tfl.fit(x=x_train, y=y_train, steps=steps)
    y_pred = tfl.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    print('TFL: R2: {0:f}, RMSE:{1:f}'.format(r2, rmse))


if __name__ == '__main__':
    fps, acts = sdf2fp('../sdf/CHEMBL3301363.sdf')
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(
        fps,
        acts,
        test_size=0.2,
        random_state=0)

    dnn(x_train, x_test, y_train, y_test, steps=10000, hidden=[200, 200])
