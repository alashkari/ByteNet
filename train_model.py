# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:25:40 2017

@author: s2410826
"""
import numpy as np
import sys

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras as ke

if __name__ == "__main__":
    
    data_path = sys.argv[1] 


    data = np.load(data_path)
    X_train = np.float32(data['X_train'])
    y_train = np.float32(data['y_train'])
    
    X_test = np.float32(data['X_test'])
    y_test = np.float32(data['y_test'])

    # Reshaping the input samples for Keras
    x_tr = X_train.reshape(X_train.shape[0], 128, 128, 1)
    x_tst = X_test.reshape(X_test.shape[0], 128, 128, 1)


    batch_size = 32
    epochs = 10

    kr_size = 4
    
    # Desiging a 4-layer CNN classifier

    # Activation function of all convolution layers is ReLU.
    # Activation function the last layers is Softmax.

    # First layer has  64 4*4 kernels. Second layer has 128 4*4 kernels.
    # Third layer has 256 4*4 kernels. Fourth layer has 512 4*4 kernels.
    # All kernel weights are initialized using Glorot (Xavier) normal initializer

    # Max poolig on 2x2 windows after convolution layers.

    # A fully-connected neural network classifies the samples, and produces the labels in the last layer.


    model = Sequential()

    model.add(Conv2D(64, kernel_size=(kr_size, kr_size), activation='relu', kernel_initializer= 'glorot_normal', input_shape=(128,128,1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (kr_size, kr_size), activation='relu', kernel_initializer= 'glorot_normal'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(256, (kr_size, kr_size), activation='relu', kernel_initializer= 'glorot_normal'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(512, (kr_size, kr_size), activation='relu', kernel_initializer= 'glorot_normal'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())

    model.add(Dense(1024, activation='relu', kernel_initializer= 'glorot_normal'))

    model.add(Dense(10, activation='softmax'))
    
    # Categorical crossentropy is selected as the loss function due to the nature of labels.
    model.compile(loss=ke.losses.categorical_crossentropy,
                  optimizer=ke.optimizers.RMSprop(),
                  metrics=['accuracy'])

    model.fit(x_tr, y_train,
              batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              validation_data=(x_tst, y_test))
    score = model.evaluate(x_tst, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    
    model.save('WAV_Classifer.h5')
