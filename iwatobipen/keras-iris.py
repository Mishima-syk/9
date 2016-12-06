from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from keras.utils.np_utils import to_categorical

# prepare dataset
irisdata = load_iris()
X,Y = irisdata["data"], irisdata["target"]
train_X, test_X, train_Y, test_Y = train_test_split( X, Y, test_size=0.2, random_state=123 )
#train_Y , test_Y = to_categorical( train_Y ), to_categorical( test_Y )

print( train_X.shape, test_X.shape )
print( test_Y.shape )

from keras.models import Sequential
model = Sequential()

# レイヤーは.addで追加して構成する
# 活性化関数や、隠れ層の設定で結果がだいぶ変わる
# 活性化関数 relu, softmax, sigmoid, tanh
from keras.layers import Dense, Activation
# 一層目の追加と活性化関数の定義
model.add( Dense( output_dim=12, input_dim=4 ) )
model.add( Activation( "relu" ) )
model.add( Dense( output_dim=3 ) )
model.add( Activation( "softmax" ) )

# モデルの生成はcompileで行う。
model.compile( optimizer="sgd",
               loss="sparse_categorical_crossentropy",
               metrics = ["accuracy"] )

hist = model.fit( train_X, train_Y, nb_epoch=50, batch_size=5 )


#　学習させたモデルで予測してみる
pred_Y = model.predict_classes( test_X )

from sklearn.metrics import confusion_matrix, classification_report
print( "CONFUSION MATRICS" )
print( confusion_matrix( test_Y, pred_Y ) )
print( "CLASSIFCATION REPORT" )
print( classification_report( test_Y, pred_Y ) )
