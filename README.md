# MUSIFY - Note Prediction Application - Model

## Computing Individual Project

### Introduction

This is the model part of the Musify application, which is a note prediction application for musicians. It is a part of the Computing Individual Project, which is a part of the BSc Software Engineering Programme at the University of Plymouth. The application is written in Python. The application uses a neural network to predict the next note in a sequence of notes. The application uses the [Magenta](https://magenta.tensorflow.org/ "Magenta") library to generate the dataset and the [TensorFlow](https://www.tensorflow.org/ "TensorFlow") library to build the neural network. The application uses the [NumPy](https://numpy.org/ "NumPy"), [SciPy](https://www.scipy.org/ "SciPy"), [Matplotlib](https://matplotlib.org/ "Matplotlib") and [Pandas](https://pandas.pydata.org/ "Pandas") libraries to process the data.

**Note: This model is only working on Ubuntu 18.04. It is not working on Windows operating systems.**

### Requirements

The application requires Python 3.8 to run. It also requires the following libraries to be installed:

- [TensorFlow 2.0](https://www.tensorflow.org/ "TensorFlow 2.0")
- [NumPy](https://numpy.org/ "NumPy")
- [SciPy](https://www.scipy.org/ "SciPy")
- [Matplotlib](https://matplotlib.org/ "Matplotlib")
- [Pandas](https://pandas.pydata.org/ "Pandas")
- [PyAudio](https://pypi.org/project/PyAudio/ "PyAudio")

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the Repository</p>

```bash
git clone https://github.com/ravindu0823/Note-Prediction
```

<p>2. Navigate to the server directory</p>

```
cd Note-Prediction/
```

<p>3. Install the Dependencies</p>

```
pip install -r requirements.txt
```

### Usage

To run the application, you can use the following command:

```bash
python app.py
```

## When Your PC has Docker Installed

<p>1. Clone the Repository</p>

```
git clone https://github.com/ravindu0823/Note-Prediction
```

<p>2. Get inside the Project</p>

```
cd Note-Prediction/
```

<p>2. Start the Docker Containers</p>

```
docker compose up -d
```
