# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:57:59 2017

@author: Amir Lashkari
ML Test
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:45:39 2017

@author: Amir Lashkari
DeepLearni.ng ML Test

"""
import sys

from os import listdir
from os.path import isfile, join

from scipy.io import wavfile
from scipy import signal
import resampy

from sklearn.model_selection import train_test_split
import numpy as np

import keras as ke

if __name__ == "__main__":
    
    mypath = sys.argv[1]  
    # mypath = 'C:\\Users\\s2410826\\Desktop\\Test\\Data'

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # adr = mypath + '\\' + onlyfiles[0]

    j=0
    FS = 4410
    X = np.zeros([(len(onlyfiles)-1),128**2])
    Y = np.zeros([(len(onlyfiles)-1),1])


    for i in range(1,(len(onlyfiles)-1)):
    
        adr = mypath + '\\' + onlyfiles[i]
    
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
        

    X[j:,:] = []
    Y[j:] = []
    print("Finished Reading & Preprocessing the dataset!!")

    # Splitting the dataset into train and test sets.
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

    # Normalizing the feature values
    X_train/=np.max(X_train)
    X_test/=np.max(X_train)
    
    # Transforming the labels into one-hot representation
    y_train = ke.utils.to_categorical(y_train, 10)
    y_test = ke.utils.to_categorical(y_test, 10)

    # Saving the preprocessed dataset for future use.
    np.savez('Variables', X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)

       
        
        
        
        
        
        
