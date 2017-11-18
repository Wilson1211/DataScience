#import nltk
import sklearn
from sklearn import datasets
from sklearn import linear_model
import pandas as pd
from sklearn.cross_validation import train_test_split
#print('The nltk version is {}.'.format(nltk.__version__))
#print('The scikit-learn version is {}.'.format(sklearn.__version__))
boston = datasets.load_boston()
#print(type(boston))
#print(boston.keys())
#print(boston.feature_names)
lr = linear_model.LinearRegression( fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)
x=boston.data
y=boston.target
print(lr.fit(x,y))
print("\n")
print(pd.DataFrame(list(zip(boston.feature_names,lr.coef_)),columns=["Feature", "Correlation"]))

"""
#print plot of x y
print
from matplotlib import pyplot as plt
plt.scatter(x[:,5], y)
plt.xlabel("Average number of room per dwelling (RM)")
plt.ylabel("Housing Price")
plt.title("Relationship between RM and Price")
plt.show()


#print("start training")
predicty=lr.predict(x)
print(predicty[0:9])
print(y[0:9])

plt.scatter(predicty, y)
plt.xlabel("Predicted Price")
plt.ylabel("Real Price")
plt.title("Relation between the predicted and real price")
plt.show()
"""

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.33)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


print("iris")
iris = datasets.load_iris()
linear_model.LogisticRegression(penalty='l2',solver='liblinear',multi_class='ovr',verbose=0,n_jobs=1)
logr = linear_model.LogisticRegression()
xtrain, xtest, ytrain, ytest = sklearn.model_selection.train_test_split(iris.data, iris.target, test_size = 0.16)

print("logr")
print(xtrain.shape)
logr.fit(xtrain,ytrain)
print(logr.score(xtrain,ytrain))
print(logr.score(xtest,ytest))

print("logr2")
logr2=linear_model.LogisticRegression(penalty='l1')
logr2.fit(xtrain,ytrain)
print(logr2.score(xtrain,ytrain))
print(logr2.score(xtest,ytest))

print("multiclass")
logr3 =linear_model.LogisticRegression(multi_class='multinomial', solver = 'newton-cg')
logr3.fit(xtrain, ytrain)
print(logr3.score(xtrain, ytrain))
print(logr3.score(xtest, ytest))

print(logr3.predict_proba(xtest[0].reshape(1, -1)))
