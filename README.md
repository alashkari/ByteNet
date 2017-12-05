# WAV_Classifier

### Prerequisite

Python 3.5 or higher is required.
You need to install these packages: os, scipy, resampy, sklearn, numpy, keras(theano backend, image_dim_ordering: "th")

### Decription

In this Project, I intend to train a model to classify short audio (.WAV) files.

To do so, I decided to apply short-time Fourier transfom (STFT) on audio samples, and pass them to a deep convolutional neural network for classification. Similiar work is done by Alex Graves for speech recognition with RNN (see https://arxiv.org/abs/1303.5778).

For loading the audio files, I used wavfile library in scipy package. However, I could not load a fraction of audio samples and I decided not to spend time on this issue.

The sampling frequency is not same for all audio files, so I converted all sampling frequencies to 4.41 KHz.
For calculating the STFT, the window length in time domain is 277 per segment. Below is the STFT of the audio file "1267-9.wav":

![stft](https://user-images.githubusercontent.com/20826407/33621947-6453ed32-d9ba-11e7-9767-417430c2a85d.png)

The CNN classifier has 4 layers.
Activation function of all convolution layers is ReLU.
Activation function the last layers is Softmax.
First layer has  64 4x4 kernels. Second layer has 128 4x4 kernels.
Third layer has 256 4x4 kernels. Fourth layer has 512 4x4 kernels.
All kernel weights are initialized using Glorot (Xavier) normal initializer.
Max poolig on 2x2 windows after convolution layers.

A fully-connected neural network classifies the samples, and produces the labels in the last layer.

### Experimental Result

For validation, the data set is devided into a training (90%) and test set (10%).

Training 10 epochs took almost 8 hours to complete on my system. 

Below, you find the training and test accuracy.
![accuracy](https://user-images.githubusercontent.com/20826407/33618511-be06be90-d9b0-11e7-99cc-756391aa7761.png)

I found that the 4.41 KHz sampling rate may be a too small, since by Nyquest theorem we won't be able to reconstruct frequencies above 2.2 KHz. I strongly suggest to try a higher sampling frequency rate.

The CNN architecture seems to be powerfull enogh to capture the hidden patterns in STFT of audio files. However, applying a RNN seems to be interesting in our problem (in this approach, the STFT may be discarded).

Although the test accuracy seems to be low, I believe that altering the sampling rate will produce a powerfull classifier.

### Running The Code

Preprocessing the data   -->   python preprocess_data.py data_directory

Training the model   -->   python train_model.py processed_data_directory
  
Testing the model   -->   python test_model.py model_path data_path p  
(p = 1 for preprocessed data and p = 0 otherwise.)

### Additional Info
These packages are used for implementing this project:

scipy (0.19.1)
resampy (0.2.0)
sklearn  (0.19.0)
numpy (1.13.3)
keras (2.0.8) (theano backend, image_dim_ordering: "th")


