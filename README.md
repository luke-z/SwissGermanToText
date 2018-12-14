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

|Text  |Amount |
|------|:-----:|
|1     |296    |
|2     |301    |
|3     |338    |
|4     |277    |
|5     |241    |
|6     |213    |
|7     |215    |
|8     |230    |
|9     |233    |
|10    |236    |
|11    |262    |
|12    |231    |

## Installation

Download [Anaconda w/ Python 3.7](https://www.anaconda.com/download/) and import the [yaml file](https://github.com/luke-z/SwissGermanToText/tree/master/resources/anacondaEnv) in the folder anacondaEnv.

## Usage

Run jupyter from the corresponding Anaconda environment and open the jupyter notebook

- Execute the import field
- Save vectors of labels to array
- Create the model
- Predict on the model

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
