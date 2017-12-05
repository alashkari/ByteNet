# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:01:12 2017

@author: Amir Lashkari
ML Test
"""

from os import listdir
from os.path import isfile, join

from scipy.io import wavfile
from scipy import signal
import resampy

import sys
import numpy as np

import keras as ke
from keras.models import load_model

if __name__ == "__main__":
    
    
    model_path = sys.argv[1] 
    data_path = sys.argv[2] 
    processed = sys.argv[3] 
    
    if processed==0:
        
        print("Loading & Preprocessing Data!!")

        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
        # adr = mypath + '\\' + onlyfiles[0]

        j=0
        FS = 4410
        X = np.zeros([(len(onlyfiles)-1),128**2])
        Y = np.zeros([(len(onlyfiles)-1),1])

        for i in range(1,(len(onlyfiles)-1)):
    
            adr = data_path + '\\' + onlyfiles[i]
    
            try:
        
                # Read WAV file from the directory
                fs, data = wavfile.read(adr)    

                # Changes the sampling rate of the WAV file into 4410 Hz
                z = resampy.resample(data[:,0], fs, FS)     
        
                # Fixing the length of all files into 4 seconds (zero padding for shorter files and cutting for longer files)
                if (data.shape[0]>(fs*4)):
                    x = z[0:(FS*4)]
                else:
                    x = np.zeros([(FS*4),1])
                    x[0:z.shape[0]] = np.reshape(z,(z.shape[0],1))
            
                # Calculatinf the short-time Fourier transform of the WAV file.
                f, t, xx = signal.stft(x[:,0], FS, nperseg=277)
        
                # Discarding the frequencies abouve 20KHz. The output will be a 128x128 matrix
                xx = xx[:128,:]
        
                # Reshaping the 128*128 matrix into a vector, and saving it with its corresponding label.
                X[j,:] = np.reshape(np.abs(xx),[np.shape(xx)[0]**2])
                Y[j] = int(onlyfiles[i][-5])
        
                j+=1
                print("sample " + repr(i) + ": Read & Preprocessed")            
    
            except:
                print("sample " + repr(i) + ": Passed")
                
                
        X = X[0:(j-1),:]
        Y =Y [0:(j-1)]
        X/=np.max(X)
        y_tst = ke.utils.to_categorical(Y, 10)      
        
                
    else:
        
        print("Loading Preprocessed Data!!")
        
        data = np.load(data_path)
    
        X = np.float32(data['X_test'])
        y_tst = np.float32(data['y_test'])

    
    # Reshaping the input samples for Keras
    x_tst = X.reshape(X.shape[0], 128, 128, 1)
        
    print("Loading Model!!")
    
    model = load_model(model_path)
    score = model.evaluate(x_tst, y_tst, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])         
        
        
