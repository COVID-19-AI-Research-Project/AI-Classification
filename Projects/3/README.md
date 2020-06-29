# Peter Moss COVID-19 AI Research Project

## COVID-19 AI Classification

### COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4

[![COVID-19 AI-Classification](../../Media/Images/covid-19-ai-classification.png)](https://github.com/COVID-19-AI-Research-Project/AI-Classification/tree/master/Projects/3)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [DISCLAIMER](#disclaimer)
- [Installation](#installation)
- [Train](#train)
  - [Start Training](#start-training)
  - [Data Processing](#data-processing)
  - [Model Summary](#model-summary)
  - [Training Results](#training-results)
  - [Metrics Overview](#metrics-overview)
  - [Figures Of Merit](#figures-of-merit)
- [Real World Testing](#real-world-testing)
  - [Local Classifier](#local-classifier)
    - [Output](#local-classifier-output)
  - [HTTP Classifier](#http-classifier)
    - [Output](#http-classifier-output)
- [Citation](#citation)
- [Contributing](#contributing)
  - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugs-issues)

&nbsp;

# Introduction

This project provides the source codes and tutorial for running a COVID-19 detection system on a Raspberry Pi 4. This project uses the trained model from [Project 2](../../Projects/2/ "Project 2") and has been modfied to work on a Raspberry Pi 4. You can either train your own model using [Project 2](../../Projects/2/ "Project 2") or you can use the pre-trained model provided.

We will be using a Tensorflow 2 implementation of DenseNet and the [SARS-COV-2 Ct-Scan Dataset](https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset "SARS-COV-2 Ct-Scan Dataset"), a large dataset of CT scans for SARS-CoV-2 (COVID-19) identification created by our collaborators, Plamenlancaster: [Professor Plamen Angelov](https://www.lancaster.ac.uk/lira/people/#d.en.397371) from [Lancaster University](https://www.lancaster.ac.uk/)/ Centre Director @ [Lira](https://www.lancaster.ac.uk/lira/), & his researcher, [Eduardo Soares PhD](https://www.lancaster.ac.uk/sci-tech/about-us/people/eduardo-almeida-soares).

&nbsp;

# DISCLAIMER

This project should be used for research purposes only. The purpose of the project is to show the potential of Artificial Intelligence for medical support systems such as diagnosis systems. Although the program is fairly accurate and shows good results both on paper and in real world testing, it is not meant to be an alternative to professional medical diagnosis. I am a self taught developer with some experience in using Artificial Intelligence for detecting certain types of cancer and COVID-19. I am not a doctor, medical or cancer/COVID-19 expert. Please use this system responsibly.

&nbsp;

# Installation

Please follow the [Installation Guide](Documentation/Installation/Installation.md) to install COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4.

&nbsp;

# Train

If you would like to train your own model, please follow the steps in [Project 2](../../Projects/2/ "Project 2"). You can run this system without training by jumping to the next step, **Real World Testing** below. If you train your own model using Project 2, you need to copy the files from the Project 2 **Model** directory to the **Model** directory in this project.

&nbsp;

# Real World Testing

On paper, our model seems to be working very well. But the real test is to use the classifier in a real world scenario. Later on we will integrate the classifier with the [HIAS UI](https://github.com/LeukemiaAiResearch/HIAS "HIAS UI"), but first we will test the classifier locally, and via HTTP requests to the endpoint that exposes the model for remote classification.

The system uses the test files specified in the configuration, as show in the [Installation Guide](../../Projects/2/Documentation/Installation/Installation.md).

## Local Classifier

First we will test our classifier locally. As we are using a Raspberry Pi, it may take a few moments to load the model. Navigate to the project root and use the following command:

```
python3 COVID19DN.py Classify
```

### Local Classifier Output

```
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         [(None, 64, 64, 3)]       0
_________________________________________________________________
conv2d (Conv2D)              (None, 64, 64, 3)         84
_________________________________________________________________
densenet121 (Model)          multiple                  7037504
_________________________________________________________________
global_average_pooling2d (Gl (None, 1024)              0
_________________________________________________________________
batch_normalization (BatchNo (None, 1024)              4096
_________________________________________________________________
dropout (Dropout)            (None, 1024)              0
_________________________________________________________________
dense (Dense)                (None, 256)               262400
_________________________________________________________________
batch_normalization_1 (Batch (None, 256)               1024
_________________________________________________________________
dropout_1 (Dropout)          (None, 256)               0
_________________________________________________________________
root (Dense)                 (None, 2)                 514
=================================================================
Total params: 7,305,622
Trainable params: 7,219,414
Non-trainable params: 86,208
_________________________________________________________________

2020-06-29 20:30:01,376 - Model - INFO - Loaded test image Model/Data/0/Non-Covid (1).png
2020-06-29 20:30:08,996 - Model - INFO - Predicted Label: 0
2020-06-29 20:30:08,997 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.9987625
2020-06-29 20:30:09,006 - Model - INFO - Loaded test image Model/Data/0/Non-Covid (54).png
2020-06-29 20:30:09,303 - Model - INFO - Predicted Label: 0
2020-06-29 20:30:09,303 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.9878852
2020-06-29 20:30:09,313 - Model - INFO - Loaded test image Model/Data/0/Non-Covid (104).png
2020-06-29 20:30:09,593 - Model - INFO - Predicted Label: 0
2020-06-29 20:30:09,594 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.9964888
2020-06-29 20:30:09,599 - Model - INFO - Loaded test image Model/Data/0/Non-Covid (389).png
2020-06-29 20:30:09,883 - Model - INFO - Predicted Label: 0
2020-06-29 20:30:09,883 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.97894233
2020-06-29 20:30:09,895 - Model - INFO - Loaded test image Model/Data/0/Non-Covid (582).png
2020-06-29 20:30:10,168 - Model - INFO - Predicted Label: 0
2020-06-29 20:30:10,168 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.86287963
2020-06-29 20:30:10,176 - Model - INFO - Loaded test image Model/Data/1/Covid (10).png
2020-06-29 20:30:10,459 - Model - INFO - Predicted Label: 1
2020-06-29 20:30:10,460 - Model - INFO - COVID-19 correctly detected (True Positive) with confidence: 0.97382665
2020-06-29 20:30:10,465 - Model - INFO - Loaded test image Model/Data/1/Covid (76).png
2020-06-29 20:30:10,745 - Model - INFO - Predicted Label: 1
2020-06-29 20:30:10,745 - Model - INFO - COVID-19 correctly detected (True Positive) with confidence: 0.99058646
2020-06-29 20:30:10,751 - Model - INFO - Loaded test image Model/Data/1/Covid (156).png
2020-06-29 20:30:11,027 - Model - INFO - Predicted Label: 1
2020-06-29 20:30:11,027 - Model - INFO - COVID-19 correctly detected (True Positive) with confidence: 0.9950991
2020-06-29 20:30:11,034 - Model - INFO - Loaded test image Model/Data/1/Covid (356).png
2020-06-29 20:30:11,301 - Model - INFO - Predicted Label: 1
2020-06-29 20:30:11,302 - Model - INFO - COVID-19 correctly detected (True Positive) with confidence: 0.96086687
2020-06-29 20:30:11,307 - Model - INFO - Loaded test image Model/Data/1/Covid (675).png
2020-06-29 20:30:11,583 - Model - INFO - Predicted Label: 0
2020-06-29 20:30:11,583 - Model - INFO - COVID-19 incorrectly not detected (False Negative) with confidence: 0.6348715
2020-06-29 20:30:11,584 - Model - INFO - Images Classified: 10
2020-06-29 20:30:11,584 - Model - INFO - True Positives: 4
2020-06-29 20:30:11,584 - Model - INFO - False Positives: 0
2020-06-29 20:30:11,584 - Model - INFO - True Negatives: 5
2020-06-29 20:30:11,584 - Model - INFO - False Negatives: 1
```

## HTTP Classifier

Next we will test our classifier server. Navigate to the project root and use the following command:

```
python3 COVID19DN.py Server
```

Then in a new terminal, navigate to the project root and issue the following command:

```
python3 COVID19DN.py Client
```

### HTTP Classifier Output

#### Server

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         [(None, 64, 64, 3)]       0
_________________________________________________________________
conv2d (Conv2D)              (None, 64, 64, 3)         84
_________________________________________________________________
densenet121 (Model)          multiple                  7037504
_________________________________________________________________
global_average_pooling2d (Gl (None, 1024)              0
_________________________________________________________________
batch_normalization (BatchNo (None, 1024)              4096
_________________________________________________________________
dropout (Dropout)            (None, 1024)              0
_________________________________________________________________
dense (Dense)                (None, 256)               262400
_________________________________________________________________
batch_normalization_1 (Batch (None, 256)               1024
_________________________________________________________________
dropout_1 (Dropout)          (None, 256)               0
_________________________________________________________________
root (Dense)                 (None, 2)                 514
=================================================================
Total params: 7,305,622
Trainable params: 7,219,414
Non-trainable params: 86,208
_________________________________________________________________

 * Serving Flask app "Classes.Server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://###.###.#.##:8181/ (Press CTRL+C to quit)

```

#### Client

```
2020-06-29 20:33:52,952 - Core - INFO - Helpers class initialization complete.
2020-06-29 20:33:52,952 - Core - INFO - COVID-19 Tensorflow DenseNet Classifier initialization complete.
2020-06-29 20:33:52,953 - Model - INFO - Sending request for: Model/Data/0/Non-Covid (1).png
2020-06-29 20:34:00,720 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.9981186985969543

2020-06-29 20:34:07,728 - Model - INFO - Sending request for: Model/Data/0/Non-Covid (54).png
2020-06-29 20:34:08,083 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.987395703792572

2020-06-29 20:34:15,090 - Model - INFO - Sending request for: Model/Data/0/Non-Covid (104).png
2020-06-29 20:34:15,463 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.9958042502403259

2020-06-29 20:34:22,470 - Model - INFO - Sending request for: Model/Data/0/Non-Covid (389).png
2020-06-29 20:34:22,830 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.9944603443145752

2020-06-29 20:34:29,837 - Model - INFO - Sending request for: Model/Data/0/Non-Covid (582).png
2020-06-29 20:34:30,205 - Model - INFO - COVID-19 correctly not detected (True Negative) with confidence: 0.9024257063865662

2020-06-29 20:34:37,212 - Model - INFO - Sending request for: Model/Data/1/Covid (10).png
2020-06-29 20:34:37,572 - Model - INFO - COVID-19 correctly detected (True Positive) with confidence: 0.9873468279838562

2020-06-29 20:34:44,579 - Model - INFO - Sending request for: Model/Data/1/Covid (76).png
2020-06-29 20:34:44,948 - Model - INFO - COVID-19 correctly detected (True Positive) with confidence: 0.9913552403450012

2020-06-29 20:34:51,955 - Model - INFO - Sending request for: Model/Data/1/Covid (156).png
2020-06-29 20:34:52,303 - Model - INFO - COVID-19 correctly detected (True Positive) with confidence: 0.9963597655296326

2020-06-29 20:34:59,311 - Model - INFO - Sending request for: Model/Data/1/Covid (356).png
2020-06-29 20:34:59,699 - Model - INFO - COVID-19 correctly detected (True Positive) with confidence: 0.9782198667526245

2020-06-29 20:35:06,707 - Model - INFO - Sending request for: Model/Data/1/Covid (675).png
2020-06-29 20:35:07,052 - Model - INFO - COVID-19 incorrectly not detected (False Negative) with confidence: 0.8346897959709167

2020-06-29 20:35:14,059 - Model - INFO - Images Classifier: 10
2020-06-29 20:35:14,060 - Model - INFO - True Positives: 4
2020-06-29 20:35:14,061 - Model - INFO - False Positives: 0
2020-06-29 20:35:14,061 - Model - INFO - True Negatives: 5
2020-06-29 20:35:14,062 - Model - INFO - False Negatives: 1
```

&nbsp;

# Citation

```
Angelov, Plamen, and Eduardo Almeida Soares. "EXPLAINABLE-BY-DESIGN APPROACH FOR COVID-19 CLASSIFICATION VIA CT-SCAN." medRxiv (2020).
Soares, Eduardo, Angelov, Plamen, Biaso, Sarah, Higa Froes, Michele, and Kanda Abe, Daniel. "SARS-CoV-2 CT-scan dataset: A large dataset of real patients CT scans for SARS-CoV-2 identification." medRxiv (2020). doi: https://doi.org/10.1101/2020.04.24.20078584.

Link:
https://www.medrxiv.org/content/10.1101/2020.04.24.20078584v2
```

&nbsp;

# Contributing

The Peter Moss COVID-19 AI Research Project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull requests. You will also find information about our code of conduct on this page.

## Contributors

- [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai/team/adam-milton-barker "Adam Milton-Barker") - [Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss](https://www.leukemiaresearchassociation.ai "Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss") President & Lead Developer, Sabadell, Spain

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](../../issues "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.
