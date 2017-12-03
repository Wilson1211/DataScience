from __future__ import print_function
import keras
from keras.datasets import cifar10
#from keras.preprocessing.image import ImageDataGenerator
#from keras.models import Sequential
#from keras.layers import Dense, Dropout, Activation, Flatten
#from keras.layers import Conv2D, MaxPooling2D
import numpy as np
import os
import pandas
import pickle



# The data, shuffled and split between train and test sets:
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
print(y_train.shape[0],'train y')
print(y_test.shape,'test y')

def load_CIFAR_batch(filename):
  """ load single batch of cifar """
  with open(filename, 'rb') as f:
    datadict = pickle.load(f,encoding='latin1')
    X = datadict['data']
    Y = datadict['labels']
    X = X.reshape(10000, 3, 32, 32).transpose(0,2,3,1).astype("float")
    Y = np.array(Y)
    return X, Y


file = "./cifar-10-batches-py/data_batch_"


for i in range(5):
	file = file + str(i+1)
	#print(file)
	(x,y) = load_CIFAR_batch(file)

	
	if(i==0):
		xtrain = x
		ytrain = y
		#print('ytrain shape:',ytrain.shape)
	else:
		xtrain = np.vstack((xtrain,x))
		#ytrain = np.vstack((ytrain,np.transpose(y)))
		ytrain = np.concatenate([ytrain,y])
		#print('ytrain shape:',ytrain.shape)

	#print(x.shape)
	#print(type(x))
	#print(y.shape)
	#print(type(y))
	file = file[0:len(file)-1]
#print(y)
print("xtrain shape:",xtrain.shape)
print('ytrain shape:',ytrain.shape)
filetest = ''



filetest = "./cifar-10-batches-py/test_batch"
(xtest,ytest) = load_CIFAR_batch(filetest)
print('xtest shape: ',xtest.shape)
print('ytest shape: ',ytest.shape)

