# WAV_Classifier

In this Project, I intend to train a model to classify short audio(.WAV) files.

To do so, I decided to apply short-time Fourier transfom (STFT) on audio samples, and pass them to a deep convolutional neural network for classification. Similiar work is done by Alex Graves for speech recognition with RNN (see https://arxiv.org/abs/1303.5778).

For loading the audio files, I used wavfile library in scipy package. However, I could not load a fraction of audio samples and I decided not to spend time on this issue.

The sampling frequency is not same for all audio files, so I converted all sampling frequencies to 44.1 KHz.
For calculating the STFT, the window length in time domain is 277 per segment.

The CNN classifier has 4 layers.
Activation function of all convolution layers is ReLU.
Activation function the last layers is Softmax.
First layer has  64 4*4 kernels. Second layer has 128 4*4 kernels.
Third layer has 256 4*4 kernels. Fourth layer has 512 4*4 kernels.
All kernel weights are initialized using Glorot (Xavier) normal initializer.
Max poolig on 2x2 windows after convolution layers.

A fully-connected neural network classifies the samples, and produces the labels in the last layer.


![accuracy](https://user-images.githubusercontent.com/20826407/33618511-be06be90-d9b0-11e7-99cc-756391aa7761.png)
