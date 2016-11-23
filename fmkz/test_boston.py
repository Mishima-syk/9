import numpy as np
import tensorflow as tf
from sklearn import cross_validation
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from math import sqrt
import random

tf.logging.set_verbosity(tf.logging.ERROR)


def dnn(x_train, x_test, y_train, y_test, steps=5000, hidden=[20, 20]):
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=13)]
    tfl = tf.contrib.learn.DNNRegressor(hidden_units=hidden, feature_columns=feature_columns)
    tfl.fit(x=x_train, y=y_train, steps=steps)
    y_pred = tfl.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    print('TFL: R2: {0:f}, RMSE:{1:f}'.format(r2, rmse))


if __name__ == "__main__":
    boston = datasets.load_boston()
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(
        boston.data, boston.target, test_size=0.2, random_state=0)

    dnn(x_train, x_test, y_train, y_test)
