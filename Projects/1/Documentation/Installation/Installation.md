# Peter Moss COVID-19 AI Research Project

## COVID-19 AI Classification

![GeniSysAI Server](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Media/Images/covid-19-ai-classification.png)

&nbsp;

# Installation & setup
The following guide will take you through setting up and installing the [AI-Classification](https://github.com/aniruddh-1/AI-Classification).

&nbsp;

# Prerequisites

## Ubuntu 18.04.4 LTS
For this Project, the operating system choice is [Ubuntu 18.04.4 LTS](https://releases.ubuntu.com/18.04.4/ "Ubuntu 18.04.4 LTS"). To get your operating system installed you can follow the [Create a bootable USB stick on Ubuntu](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-ubuntu#0 "Create a bootable USB stick on Ubuntu") tutorial.

## Python3 & Tensorflow2
Ubuntu 18.04 come with Python 3.6 by default. You should be able to invoke it with the command in Shell:
```
python3
```
**The installation can be run on an existing installation of Ubuntu, however we recommend using a fresh installation.**
If you face any error or problem while running above command, follow the below commands:
```
sudo apt-get update
sudo apt-get install python3.6
```
You can then invoke it with the command:
```
python3.6
```
Now install the required remaining Python libraries and Tensorflow2 on system by following shell commands:
```
pip install numpy
pip install pickle-mixin
pip install os-sys
pip install times
pip install h5py
pip install random2
pip install tensorflow==2.1.0
pip install tensorflow-gpu==2.1.0
pip install tensorboard==2.1.0
```
## Quick Install
To do a continuous install after installing Python3.6, use the following command from the Projects/1:
```
sh Scripts/Installation/Shell/Install.sh
```

# Clone the repository

Clone the [AI-Classification](https://github.com/COVID-19-AI-Research-Project/AI-Classification "AI-Classification") repository from the [Peter Moss Acute Myeloid & Lymphoblastic COVID-19 AI Research Project](https://github.com/COVID-19-AI-Research-Project "Peter Moss COVID-19 AI Research Project") Github Organization.

To clone the repository and install the COVID19 AI Quantum Tensorflow repository, make sure you have Git installed. Now navigate to the location you want to clone the repository to on your device using terminal/commandline, and then use the following command.

The **-b "0.1.0"** parameter ensures you get the code from the latest development branch. Before using the below command please check our latest development branch in the button at the top of this page.

```
  $ git clone -b "0.1.0" https://github.com/COVID-19-AI-Research-Project/AI-Classification.git
```

Once you have used the command above you will see a directory called **AI-Classification** in the location you chose to clone to. In terminal, navigate to the **AI-Classification** directory, this is your project root directory.

## Repository Motivation
The following repository can be used for following purposes:
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
-Open your browser and navigate to shown web address in shell. In our case we gave many values to the list of parameters and the tensorboard tab was recorded with the following results:
![GeniSysAI Server](https://github.com/aniruddh-1/AI-Classification/tree/0.1.0/Projects/1/Media/Images/tensorboard_log.png)

## Developer Forks
Developers from the Github community that would like to contribute to the development of this project should first create a fork, and clone that repository. For detailed information please view the [CONTRIBUTING](https://github.com/COVID-19-AI-Research-Project/COVID19-AI-Quantum-Tensorflow/blob/master/CONTRIBUTING.md "CONTRIBUTING") guide.

&nbsp;

# Contributing

The Peter Moss Acute Myeloid & Lymphoblastic Leukemia AI Research project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull requests. You will also find information about our code of conduct on this page.

## Contributors

- **PROJECT AUTHOR:** [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai.com/team/adam-milton-barker "Adam Milton-Barker") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") Founder & Intel Software Innovator, Sabadell, Spain

- **PROJECT AUTHOR:** [Aniruddh Sharma](https://www.leukemiaresearchassociation.ai.com/team/AniruddhSharma "Aniruddh Sharma") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") R&D, Ahmedabad, India

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](../../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/Media/Images/repo-issues.png "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](https://github.com/aniruddh-1/AI-Classification/blob/0.1.0/CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.