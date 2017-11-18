import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn import neural_network
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
#scaler = StandardScaler()
#scaler.fit(X_train)
#X_train = scaler.transform(X_train)
#X_test = scaler.transform(X_test)
StandardScaler(copy=True, with_mean=True,with_std=True)

sklearn.neural_network.MLPClassifier(
hidden_layer_sizes=(100,),
activation='relu',
solver='adam',
alpha=0.0001,
batch_size='auto',
learning_rate='constant',
learning_rate_init=0.001,
max_iter=400,
shuffle=True,
momentum=0.9,)

#sklearn.neural_network.MLPClassifier(solver="adam")

iris = datasets.load_iris()

scalar=StandardScaler()

Xtrain, Xtest, ytrain, ytest = sklearn.model_selection.train_test_split(iris.data, iris.target, test_size = 0.165)

scalar.fit(Xtrain)
Xtrain2 = scalar.transform(Xtrain)
Xtest2 = scalar.transform(Xtest)
mlp = MLPClassifier(solver="adam",max_iter=400)
mlp.fit(Xtrain, ytrain)
print(mlp.score(Xtrain, ytrain))
print(mlp.score(Xtest, ytest))
