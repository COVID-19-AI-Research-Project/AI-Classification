# Peter Moss COVID-19 AI Research Project
## COVID-19 AI Classification
[![COVID-19 AI-Classification](../../Media/Images/covid-19-ai-classification.png)](https://github.com/COVID-19-AI-Research-Project/AI-Classification)

&nbsp;

# Introduction
![GeniSysAI Server](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Media/Images/tensorflow.png)
TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.

TensorFlow was originally developed by researchers and engineers working on the Google Brain team within Google's Machine Intelligence Research organization to conduct machine learning and deep neural networks research. The system is general enough to be applicable in a wide variety of other domains, as well.

TensorFlow provides stable Python and C++ APIs, as well as non-guaranteed backward compatible API for other languages.

We will be using Tensorflow 2.1.0 with Python3 for detecting Covid-19 Pneumonia signs from CT Scan Images by a CNN(Convolutional Neural Network) Model. The model have a uniform dataset of 764 Images of CT Scan which consist 349 Images of Covid-19 Pneumonia affected patients and remaining shows normal patient scans.

## Installation
Please follow the [Installation Guide](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Documentation/Installation/Installation.md) to install COVID-19 AI Classification Tensorflow.

## Project Motivation
The Project can be used for following purposes:
1. **Training a CNN model on the given Image Dataset** 
 - Unzip the provided CT Scan Image [dataset](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/ct_scans_png_dataset.rar) provided in Classes directory **or** you can also generate or import any other CT Scan dataset in this directory with same directory structure as in unzipped [dataset](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/ct_scans_png_dataset.rar) folder.
 - Use [dataset_preparation.py](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/dataset_preparation.py) to resize all the images into 150x150 Pixels, then converting the PNG format dataset and their labels(covid19 or normal) into Pickle as the Model will take them in form of pickle dataset.
 - The above program will generate two pickle files(X.pickle, Y.pickle) in same [Classes](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/ct_scans_png_dataset.rar) directory, we have also provided generated pickle files for same [dataset](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/ct_scans_png_dataset.rar), so that you can use these pickle files directly in generating CNN Model by using [__init__.py](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/__init__.py).
 - The program([__init__.py](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/__init__.py)) will generate a saved model file and a tensorboard log file which shows the performance of model loss and accuracy in scalar graph.

 **Note:** Use [rename_image_and_filetype_conversion.py](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/rename_image_and_filetype_conversion.py) for making all images in same format(PNG) and indexed as it is possible that while using a new or any open source CT Scan Image dataset in Step 1, all may not be in same Image format and Indexed properly.

2. **Predicting CT Scan Image**
 - After training the model on the dataset, use [predict_ct_scan.py](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/predict_ct_scan.py) to test on any lung ct scan image, the program will first resize the image to 150 x 150 pixel size, then loads the image into model and print the type of scan(Covid-19 or Normal Scan). It should be noted that the prediction of model is based on these parameters: Training Accuracy, Training Loss, Validation Accuracy and Validation Loss for the given dataset and the trained model architecture.

3. **Using Tensorboard for Optimization, Analysing and Selection of CNN Architectures**
 - Add/Change the parameters for conv_layers, conv_sizes and dense_layers of [__init__.py](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/__init__.py) and run it in shell(Comment the last line of program if you don't want to save the trained model) in [Classes](https://github.com/aniruddh-1/AI-Classification/tree/0.1.0/Projects/1/Classes) Directory.
 - A new folder named: "logs" will be genearated in the same Directory. Now run shell in same [Classes](https://github.com/aniruddh-1/AI-Classification/tree/0.1.0/Projects/1/Classes) directory again and execute the following command:
 ```
 tensorboard --logdir logs
 ```
Open your browser and navigate to shown web address in shell. In our case we gave many values to the list of parameters and the tensorboard tab was recorded with the following results:

![GeniSysAI Server](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Media/Images/tensorboard_log.png)


# COVID19-AI-Detection
Open source Artificial Intelligence (CNNs &amp; GANs) for COVID-19 Pneumonia detection/early detection.

Detects Covid-19 Pneumonia signs from CT Scan Images by a CNN Model. The model have a uniform dataset of 764 Images of CT Scan which consist 349 Images of Covid-19 Pneumonia affected patients and remaining shows normal patient scans.

Here are some CT-Scans of lungs:

COVID19 Patient Scan:

![alt text](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Media/Images/covid19_ct_scan.png "CT Scan1")






Normal Patient Scan:

![alt text](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Media/Images/normal_ct_scan.png "CT Scan2")

The dataset was taken from the following [source](https://github.com/UCSD-AI4H/COVID-CT/tree/master/Images-processed).
You can go through our [dataset](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Projects/1/Classes/ct_scans_png_dataset.rar) where we have indexed all the images and converted them into same format(PNG).
We have used tensorflow library for training a binary classification model of CT Scans using Convolutional Neural Network. The graph of model is as follows:

![alt text](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Media/Images/cnn_architecture.png "CNN")

We have also uploaded 2 trained models on above graphs:
* Model 1: Validation Accuracy - 80.82%, Validation Loss - 50.10%
* Model 2: Validation Accuracy - 78.00%, Validation Loss - 47.28%

As the dataset of CT Scans of COVID19 patients is limited, the model seems to overfit, you can  follow the instructions for contributing on [CONTRIBUTING.md](../../CONTRIBUTING.md "CONTRIBUTING.md")

&nbsp;

# Contributing

The Peter Moss Acute Myeloid & Lymphoblastic Leukemia AI Research project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull requests. You will also find information about our code of conduct on this page.

## Contributors

- **PROJECT AUTHOR:** [Aniruddh Sharma](https://www.leukemiaresearchassociation.ai.com/team/AniruddhSharma "Aniruddh Sharma") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") R&D, Ahmedabad, India

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Media/Images/repo-issues.png "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.