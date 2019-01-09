![Deep Learning](https://github.com/luke-z/SwissGermanToText/blob/master/resources/img/header.jpg)

<h1 align="center">SwissGermanToText</h1>

This is a school project in which we make a deep learning application able to translate spoken Swiss German to text.

<h4 align="center">Team:</h4>
<p align="center">Lukas Zbinden | Olivier Gafner | Katrin Horn</p>

## Baseline information

- The training and test set split is 60 / 40 with a seed of 42.
- Current accuracy: ~0.92.

Parameters:

```python
feature_dim_1 = 20
feature_dim_2 = 11
channel = 1
epochs = 50
batch_size = 100
verbose = 1
```

Model parameters:

```python
model = Sequential()
    model.add(Conv2D(32, kernel_size=(2, 2), activation='relu', input_shape=(feature_dim_1, feature_dim_2, channel)))
    model.add(Conv2D(48, kernel_size=(2, 2), activation='relu'))
    model.add(Conv2D(120, kernel_size=(2, 2), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])
```

The baseline model can be found [here](https://github.com/luke-z/SwissGermanToText/tree/master/models)

#### Amount of audio samples:
All audio samples are recorded with 44.1kHz

|Text  |Amount Baseline | Amount After Improvement II |
|------|:--------------:|:---------------------------:|
|1     |296             |330                          |
|2     |301             |335                          |
|3     |338             |370                          |
|4     |277             |307                          |
|5     |241             |272                          |
|6     |213             |242                          |
|7     |215             |249                          |
|8     |230             |261                          |
|9     |233             |264                          |
|10    |236             |267                          |
|11    |262             |294                          |
|12    |231             |266                          |

## Improvement I

For the first improvement we tried a few separate things:

- **Increasing the feature_dim_2 variable:** \
 this led to a higher accuracy on the test set, but dramatically decreased the number recognition on new data.
- **Increase the amount of epochs:** \
 When we went over ~40 epochs, there was no more improvement to the accuracy. It might even have decreased the accuracy on 
 never seen before data due to overfitting.
- **Changing the batch size:** \
 By decreasing the batch size we achieved a higher accuracy on never seen before data. The only downside is the extremely 
 high amount of time it takes until the model is trained.

*At the end of Improvement I we were on an accuracy of about 0.92. The recognition on new data was about 90% aswell.*

## Improvement II

The second improvement involved changes to the dataset & layers:

- **We added new data to our dataset**: 
  * We added additional male audio samples, which increased the recognition of unseen data a little bit. 
  * By adding female voice samples for each number, we had a new obstacle since the amount of that kind of data is pretty 
 low compared to male voices.
- **Changes to the layers:** 
  * By adding a GaussianNoise layer we tried to add some noise to our data set. Before adding the new audio samples, it 
 performed pretty well by increasing our accuracy. Afterwards, there was no more visible improvement. 
  * Increasing the dropout by a factor of two on the first dropout instance decreased the accuracy dramatically.

*At the end of Improvement II the accuracy dropped to about 0.88 for the test set. The recognition on new data dropped to about 50%*

## Learnings

- By recording and preparing all the samples ourselves, we realized what kind of effort it takes to create useful data for machine learning.
- There is a huge amount of data samples needed, particularly with the deep learning approach.
- It is very hard to tweak the right hyperparameter, especially when you cannot see under the hood as experienced in this project.
- A small deviation from test data in regard to the previously used training data can already have a huge impact on how accurate the prediction is.

## Installation

Download [Anaconda w/ Python 3.7](https://www.anaconda.com/download/) and import the [yaml file](https://github.com/luke-z/SwissGermanToText/tree/master/resources/anacondaEnv) in the folder anacondaEnv.

## Local Usage

Run jupyter from the corresponding Anaconda environment and open the jupyter notebook

- Execute the import field
- Save vectors of labels to array
- Create the model
- Predict on the model

## Colab Usage

1. Open the [Google Colab Notebook](https://colab.research.google.com/drive/1G6XVTkENH5_0OCO945xyd88YCoaGc-Hl).
2. Click on "playground mode" to start using the notebook.
3. Clone the git repo and start trying out things.

## Important packages

These are the important packages we are using:

| Package    |
| -----------|
| librosa    |
| sklearn    |
| keras      |
| numpy      |
| os         |
| matplotlib |

The rest can be found in the exported environment file

## Sources
#### Speech recognition part:
- [DeadSimpleSpeechRecognizer](https://github.com/manashmndl/DeadSimpleSpeechRecognizer)
- [Keras history & report](https://www.kaggle.com/danbrice/keras-plot-history-full-report-and-grid-search)
- [Keras save & load model](https://www.pyimagesearch.com/2018/12/10/keras-save-and-load-your-deep-learning-models/)
- [Keras Sequential model](https://keras.io/getting-started/sequential-model-guide/)

#### Programs used for audio data creation:
- [Audacity](https://www.audacityteam.org/download/)
- [WavePad Sound Editor](https://www.nch.com.au/wavepad/index.html)
