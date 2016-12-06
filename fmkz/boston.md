

```python
import tensorflow as tf
from sklearn import cross_validation
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from math import sqrt
```


```python
def dnn(x_train, x_test, y_train, y_test, steps=1000, hidden=[20, 20]):
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=13)]
    tfl = tf.contrib.learn.DNNRegressor(hidden_units=hidden,
                                        feature_columns=feature_columns,
                                        model_dir="./boston_model")

    tfl.fit(x=x_train, y=y_train, steps=steps)
    y_pred = tfl.predict(x_test)
    r2 = r2_score(y_test, y_pred)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    print('TFL: R2: {0:f}, RMSE:{1:f}'.format(r2, rmse))
```


```python
boston = datasets.load_boston()
```


```python
boston
```




    {'DESCR': "Boston House Prices dataset\n\nNotes\n------\nData Set Characteristics:  \n\n    :Number of Instances: 506 \n\n    :Number of Attributes: 13 numeric/categorical predictive\n    \n    :Median Value (attribute 14) is usually the target\n\n    :Attribute Information (in order):\n        - CRIM     per capita crime rate by town\n        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.\n        - INDUS    proportion of non-retail business acres per town\n        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)\n        - NOX      nitric oxides concentration (parts per 10 million)\n        - RM       average number of rooms per dwelling\n        - AGE      proportion of owner-occupied units built prior to 1940\n        - DIS      weighted distances to five Boston employment centres\n        - RAD      index of accessibility to radial highways\n        - TAX      full-value property-tax rate per $10,000\n        - PTRATIO  pupil-teacher ratio by town\n        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town\n        - LSTAT    % lower status of the population\n        - MEDV     Median value of owner-occupied homes in $1000's\n\n    :Missing Attribute Values: None\n\n    :Creator: Harrison, D. and Rubinfeld, D.L.\n\nThis is a copy of UCI ML housing dataset.\nhttp://archive.ics.uci.edu/ml/datasets/Housing\n\n\nThis dataset was taken from the StatLib library which is maintained at Carnegie Mellon University.\n\nThe Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic\nprices and the demand for clean air', J. Environ. Economics & Management,\nvol.5, 81-102, 1978.   Used in Belsley, Kuh & Welsch, 'Regression diagnostics\n...', Wiley, 1980.   N.B. Various transformations are used in the table on\npages 244-261 of the latter.\n\nThe Boston house-price data has been used in many machine learning papers that address regression\nproblems.   \n     \n**References**\n\n   - Belsley, Kuh & Welsch, 'Regression diagnostics: Identifying Influential Data and Sources of Collinearity', Wiley, 1980. 244-261.\n   - Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning. In Proceedings on the Tenth International Conference of Machine Learning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.\n   - many more! (see http://archive.ics.uci.edu/ml/datasets/Housing)\n",
     'data': array([[  6.32000000e-03,   1.80000000e+01,   2.31000000e+00, ...,
               1.53000000e+01,   3.96900000e+02,   4.98000000e+00],
            [  2.73100000e-02,   0.00000000e+00,   7.07000000e+00, ...,
               1.78000000e+01,   3.96900000e+02,   9.14000000e+00],
            [  2.72900000e-02,   0.00000000e+00,   7.07000000e+00, ...,
               1.78000000e+01,   3.92830000e+02,   4.03000000e+00],
            ..., 
            [  6.07600000e-02,   0.00000000e+00,   1.19300000e+01, ...,
               2.10000000e+01,   3.96900000e+02,   5.64000000e+00],
            [  1.09590000e-01,   0.00000000e+00,   1.19300000e+01, ...,
               2.10000000e+01,   3.93450000e+02,   6.48000000e+00],
            [  4.74100000e-02,   0.00000000e+00,   1.19300000e+01, ...,
               2.10000000e+01,   3.96900000e+02,   7.88000000e+00]]),
     'feature_names': array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
            'TAX', 'PTRATIO', 'B', 'LSTAT'], 
           dtype='<U7'),
     'target': array([ 24. ,  21.6,  34.7,  33.4,  36.2,  28.7,  22.9,  27.1,  16.5,
             18.9,  15. ,  18.9,  21.7,  20.4,  18.2,  19.9,  23.1,  17.5,
             20.2,  18.2,  13.6,  19.6,  15.2,  14.5,  15.6,  13.9,  16.6,
             14.8,  18.4,  21. ,  12.7,  14.5,  13.2,  13.1,  13.5,  18.9,
             20. ,  21. ,  24.7,  30.8,  34.9,  26.6,  25.3,  24.7,  21.2,
             19.3,  20. ,  16.6,  14.4,  19.4,  19.7,  20.5,  25. ,  23.4,
             18.9,  35.4,  24.7,  31.6,  23.3,  19.6,  18.7,  16. ,  22.2,
             25. ,  33. ,  23.5,  19.4,  22. ,  17.4,  20.9,  24.2,  21.7,
             22.8,  23.4,  24.1,  21.4,  20. ,  20.8,  21.2,  20.3,  28. ,
             23.9,  24.8,  22.9,  23.9,  26.6,  22.5,  22.2,  23.6,  28.7,
             22.6,  22. ,  22.9,  25. ,  20.6,  28.4,  21.4,  38.7,  43.8,
             33.2,  27.5,  26.5,  18.6,  19.3,  20.1,  19.5,  19.5,  20.4,
             19.8,  19.4,  21.7,  22.8,  18.8,  18.7,  18.5,  18.3,  21.2,
             19.2,  20.4,  19.3,  22. ,  20.3,  20.5,  17.3,  18.8,  21.4,
             15.7,  16.2,  18. ,  14.3,  19.2,  19.6,  23. ,  18.4,  15.6,
             18.1,  17.4,  17.1,  13.3,  17.8,  14. ,  14.4,  13.4,  15.6,
             11.8,  13.8,  15.6,  14.6,  17.8,  15.4,  21.5,  19.6,  15.3,
             19.4,  17. ,  15.6,  13.1,  41.3,  24.3,  23.3,  27. ,  50. ,
             50. ,  50. ,  22.7,  25. ,  50. ,  23.8,  23.8,  22.3,  17.4,
             19.1,  23.1,  23.6,  22.6,  29.4,  23.2,  24.6,  29.9,  37.2,
             39.8,  36.2,  37.9,  32.5,  26.4,  29.6,  50. ,  32. ,  29.8,
             34.9,  37. ,  30.5,  36.4,  31.1,  29.1,  50. ,  33.3,  30.3,
             34.6,  34.9,  32.9,  24.1,  42.3,  48.5,  50. ,  22.6,  24.4,
             22.5,  24.4,  20. ,  21.7,  19.3,  22.4,  28.1,  23.7,  25. ,
             23.3,  28.7,  21.5,  23. ,  26.7,  21.7,  27.5,  30.1,  44.8,
             50. ,  37.6,  31.6,  46.7,  31.5,  24.3,  31.7,  41.7,  48.3,
             29. ,  24. ,  25.1,  31.5,  23.7,  23.3,  22. ,  20.1,  22.2,
             23.7,  17.6,  18.5,  24.3,  20.5,  24.5,  26.2,  24.4,  24.8,
             29.6,  42.8,  21.9,  20.9,  44. ,  50. ,  36. ,  30.1,  33.8,
             43.1,  48.8,  31. ,  36.5,  22.8,  30.7,  50. ,  43.5,  20.7,
             21.1,  25.2,  24.4,  35.2,  32.4,  32. ,  33.2,  33.1,  29.1,
             35.1,  45.4,  35.4,  46. ,  50. ,  32.2,  22. ,  20.1,  23.2,
             22.3,  24.8,  28.5,  37.3,  27.9,  23.9,  21.7,  28.6,  27.1,
             20.3,  22.5,  29. ,  24.8,  22. ,  26.4,  33.1,  36.1,  28.4,
             33.4,  28.2,  22.8,  20.3,  16.1,  22.1,  19.4,  21.6,  23.8,
             16.2,  17.8,  19.8,  23.1,  21. ,  23.8,  23.1,  20.4,  18.5,
             25. ,  24.6,  23. ,  22.2,  19.3,  22.6,  19.8,  17.1,  19.4,
             22.2,  20.7,  21.1,  19.5,  18.5,  20.6,  19. ,  18.7,  32.7,
             16.5,  23.9,  31.2,  17.5,  17.2,  23.1,  24.5,  26.6,  22.9,
             24.1,  18.6,  30.1,  18.2,  20.6,  17.8,  21.7,  22.7,  22.6,
             25. ,  19.9,  20.8,  16.8,  21.9,  27.5,  21.9,  23.1,  50. ,
             50. ,  50. ,  50. ,  50. ,  13.8,  13.8,  15. ,  13.9,  13.3,
             13.1,  10.2,  10.4,  10.9,  11.3,  12.3,   8.8,   7.2,  10.5,
              7.4,  10.2,  11.5,  15.1,  23.2,   9.7,  13.8,  12.7,  13.1,
             12.5,   8.5,   5. ,   6.3,   5.6,   7.2,  12.1,   8.3,   8.5,
              5. ,  11.9,  27.9,  17.2,  27.5,  15. ,  17.2,  17.9,  16.3,
              7. ,   7.2,   7.5,  10.4,   8.8,   8.4,  16.7,  14.2,  20.8,
             13.4,  11.7,   8.3,  10.2,  10.9,  11. ,   9.5,  14.5,  14.1,
             16.1,  14.3,  11.7,  13.4,   9.6,   8.7,   8.4,  12.8,  10.5,
             17.1,  18.4,  15.4,  10.8,  11.8,  14.9,  12.6,  14.1,  13. ,
             13.4,  15.2,  16.1,  17.8,  14.9,  14.1,  12.7,  13.5,  14.9,
             20. ,  16.4,  17.7,  19.5,  20.2,  21.4,  19.9,  19. ,  19.1,
             19.1,  20.1,  19.9,  19.6,  23.2,  29.8,  13.8,  13.3,  16.7,
             12. ,  14.6,  21.4,  23. ,  23.7,  25. ,  21.8,  20.6,  21.2,
             19.1,  20.6,  15.2,   7. ,   8.1,  13.6,  20.1,  21.8,  24.5,
             23.1,  19.7,  18.3,  21.2,  17.5,  16.8,  22.4,  20.6,  23.9,
             22. ,  11.9])}




```python
x_train, x_test, y_train, y_test = cross_validation.train_test_split(
        boston.data, boston.target, test_size=0.2, random_state=0)
```


```python
dnn(x_train, x_test, y_train, y_test)
```

    WARNING:tensorflow:Change warning: default value of `enable_centered_bias` will change after 2016-10-09. It will be disabled by default.Instructions for keeping existing behaviour:
    Explicitly set `enable_centered_bias` to 'True' if you want to keep existing behaviour.
    WARNING:tensorflow:Using default config.
    WARNING:tensorflow:float64 is not supported by many models, consider casting to float32.
    WARNING:tensorflow:float64 is not supported by many models, consider casting to float32.
    WARNING:tensorflow:Calling BaseEstimator.predict (from tensorflow.contrib.learn.python.learn.estimators.estimator) with as_iterable=False is deprecated and will be removed after 2016-09-15.
    Instructions for updating:
    The default behavior of predict() is changing. The default value for
    as_iterable will change to True, and then the flag will be removed
    altogether. The behavior of this flag is described below.
    WARNING:tensorflow:float64 is not supported by many models, consider casting to float32.


    TFL: R2: 0.647669, RMSE:5.356281



```python

```
