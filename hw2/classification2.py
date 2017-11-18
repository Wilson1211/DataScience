import csv
import sys
import sklearn
from sklearn import datasets
from sklearn.cross_validation import train_test_split
import numpy as np

# for linear regression
from sklearn import linear_model
import pandas as pd

# for Decision tree
from sklearn import svm
from sklearn import tree
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

# for SVM
from sklearn.grid_search import GridSearchCV

# for Neural Network
from sklearn.preprocessing import StandardScaler
from sklearn import neural_network
from sklearn.neural_network import MLPClassifier
command=sys.argv[1]
#input_file = "train.csv"
#"""
input_file = sys.argv[2]
test_file = sys.argv[3]
print("filename")
print(input_file)
print(test_file)
#"""
df = pd.read_csv(input_file,header=None)
numpy_array = df.as_matrix()
print ("numpy_array:")
print(numpy_array.shape)

xtrain = numpy_array[:,0:numpy_array.shape[1]-1]
ytrain = numpy_array[:,numpy_array.shape[1]-1]
print("xtrain.shape:")
print(xtrain.shape)
print("ytrain.shape:")
print(ytrain.shape)

input_file = "test.csv"

df = pd.read_csv(input_file,header=None)
numpy_array = df.as_matrix()

xtest = numpy_array[:,0:numpy_array.shape[1]]
#ytest = numpy_array[:,numpy_array.shape[1]-1]
print("xtest.shape:")
print(xtest.shape)
#print("ytest.shape:")
#print(ytest.shape)

#lr = linear_model.LinearRegression( fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)
#lr.fit(xtrain,ytrain)

# for testing from train.csv
traincx,testcx,traincy,testcy = sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.15)


if command=="R":
	#print("Regression")
	logr = linear_model.LogisticRegression(penalty='l2',solver='liblinear',multi_class='ovr',verbose=0,n_jobs=1)
	logr.fit(xtrain,ytrain)
	predictY=logr.predict(xtest)
	
	# for test
	logr_test = linear_model.LogisticRegression(penalty='l2',solver='liblinear',multi_class='ovr',verbose=0,n_jobs=1)
	logr_test.fit(traincx,traincy)
	print("R in test")
	print(logr_test.score(testcx,testcy))


elif command=="D":
	#print("DT")
	sklearn.tree.DecisionTreeClassifier(
	criterion='gini',
	splitter='best',
	max_depth=None,
	min_samples_split=2,
	max_features=None,
	max_leaf_nodes=None,
	min_impurity_decrease=0.0)

	#xtrain, xtest, ytrain, ytest =sklearn.model_selection.train_test_split(iris.data,iris.target, test_size = 0.17)
	dct = sklearn.tree.DecisionTreeClassifier()
	dct.fit(xtrain, ytrain)
	predictY=dct.predict(xtest)
	
	# for test
	dctest = sklearn.tree.DecisionTreeClassifier()
	dctest.fit(traincx,traincy)
	print("D in test")
	print(dctest.score(testcx,testcy))

elif command=="S" :
	#svc_model=sklearn.svm.SVC(gamma=0.001, C=100.,kernel='linear')

#	svc_model=sklearn.svm.SVC()
#	svc_model.fit(xtrain, ytrain)

#	predictY=svc_model.predict(xtest)

	#parameter_candidates = [{'C': [1, 10,100,1000]}]#, 'kernel': ['linear','rbf']}]#,
        #{'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001],
        #'kernel': ['rbf']},]
	parameter_candidates = [{'C': [1,10,100,1000], 'gamma': [0.001,0.0001],'kernel': ['rbf']}]
	clf = GridSearchCV(estimator=svm.SVC(),param_grid=parameter_candidates, n_jobs=-1)
        #clf.fit(xtrain, ytrain)


	# for test
	#svc_model_test=sklearn.svm.SVC()
	clf.fit(traincx,traincy)
	predictY=clf.predict(xtest)
	print("S in test")
	print(clf.score(testcx,testcy))
	
elif command=="N" :
	#print("Neural Network")
	StandardScaler(copy=True, with_mean=True,with_std=True)

	sklearn.neural_network.MLPClassifier(
	hidden_layer_sizes=(100,),
	activation='relu',
	solver='adam',
	alpha=0.0001,
	batch_size='auto',
	learning_rate='constant',
	learning_rate_init=0.001,
	max_iter=200,
	shuffle=True,
	momentum=0.9,)

	#sklearn.neural_network.MLPClassifier(solver="adam")

	scalar=StandardScaler()

	#Xtrain, Xtest, ytrain, ytest = sklearn.model_selection.train_test_split(iris.data, iris.target, test_size = 0.165)
	scalar.fit(xtrain)
	Xtrain2 = scalar.transform(xtrain)
	Xtest2 = scalar.transform(xtest)
	mlp = MLPClassifier(solver="adam",max_iter=200)
	mlp.fit(xtrain, ytrain)
	predictY=mlp.predict(Xtest2)
	
	# for test
	scalar_test=StandardScaler()
	scalar_test.fit(traincx)
	traincx2=scalar_test.transform(traincx)
	testcx2 = scalar_test.transform(testcx)
	mlp_test = MLPClassifier(solver="adam",max_iter=200)
	mlp_test.fit(traincx,traincy)
	print("N in test")
	print(mlp_test.score(testcx,testcy))
	print("after scalar")
	mlp_test.fit(traincx2,traincy)
	print(mlp_test.score(testcx2,testcy))
		
else:
	print("wrong input method")

pd.DataFrame(predictY).to_csv('prediction.csv',index=False,header=False)
