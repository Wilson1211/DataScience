import sklearn
from sklearn import svm
from sklearn import datasets
from sklearn.grid_search import GridSearchCV
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import numpy as np
digit = datasets.load_digits()
print(digit.keys())
x=digit.data
y=digit.target
xtrain,xtest,ytrain,ytest = sklearn.model_selection.train_test_split(x,y,test_size=0.30)#順序很重要
#print(xtrain.shape)
#print(ytrain.shape)
print(digit.data.shape)
print(np.unique(digit.target))
sklearn.svm.SVC(C=1.0,kernel='rbf',degree=3,gamma='auto',decision_function_shape='ovr')
svc_model = sklearn.svm.SVC(gamma=0.001, C=100.,kernel='linear')
svc_model.fit(xtrain, ytrain)
print(svc_model.score(xtrain, ytrain))
print(svc_model.score(xtest, ytest))

parameter_candidates = [
{'C': [1, 10, 100, 1000], 'kernel': ['linear']},
{'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001],
'kernel': ['rbf']},]
clf = GridSearchCV(estimator=svm.SVC(),param_grid=parameter_candidates, n_jobs=-1)
clf.fit(xtrain, ytrain)

print(clf.score(xtrain,ytrain))
print(clf.score(xtest,ytest))

print('Best score for training data:',clf.best_score_)
print('Best `C`:',clf.best_estimator_.C)
print('Best kernel:',clf.best_estimator_.kernel)
print('Best `gamma`:',clf.best_estimator_.gamma)

print("PCA")
pca = PCA(n_components = 2)
pca.fit(digit.data)
pdata = pca.transform(digit.data)
plt.scatter(pdata[:,0],pdata[:,1])
plt.show()
#print(pdata.shape)
#print(y.shape)
