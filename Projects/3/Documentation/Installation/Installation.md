# Peter Moss COVID-19 AI Research Project

## COVID-19 AI Classification

### COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4

[![GeniSysAI Server](../../../../Media/Images/covid-19-ai-classification.png)](https://github.com/COVID-19-AI-Research-Project/AI-Classification/tree/master/Projects/3)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [Required Hardware](#required-hardware)
- [Prerequisites](#prerequisites)
  - [HIAS](#hias)
  - [Raspberry Pi Buster](#raspberry-pi-buster)
  - [Clone the repository](#clone-the-repository)
    - [Developer Forks](#developer-forks)
- [Installation](#installation)
  - [Easy Install](#easy-install)
  - [Manual Install](#manual-install)
- [Data](#data)
  - [Test Data](#test-data)
- [iotJumpWay](#iotjumpway)
  - [ipinfo](#ipinfo)
- [Continue](#continue)
- [Contributing](#contributing)
  - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugs-issues)

&nbsp;

# Introduction

The following guide will take you through setting up and installing the [ COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4](https://github.com/COVID-19-AI-Research-Project/AI-Classification/tree/master/Projects/3 " COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4").

&nbsp;

# Prerequisites

## HIAS

This project requires a fully functioning [HIAS](https://github.com/LeukemiaAiResearch/HIAS "HIAS") server. Features of this project require the iotJumpWay for device to device/application communication. The iotJumpWay broker is part of the HIAS server and must be running for the system to work correctly. 

Before you start this tutorial please complete the [HIAS Installation Guide](https://github.com/LeukemiaAiResearch/HIAS/blob/master/Documentation/Installation/Installation.md "HIAS Installation Guide").

If you want to use this project without HIAS you can comment out the following lines in **COVID19DN.py**:

```
COVID19DN.iotjumpway_client()
COVID19DN.threading()
```

## Raspberry Pi Buster

For this Project, the operating system choice is [Raspberry Pi Buster](https://www.raspberrypi.org/downloads/raspberry-pi-os/ "Raspberry Pi Buster"), previously known as Raspian. 

## Python3

Ubuntu 18.04 come with Python 3.6 by default. You should be able to invoke it with the command in Shell:

```
python3
```

## Clone the repository

Clone the [COVID-19 AI Classification](https://github.com/COVID-19-AI-Research-Project/AI-Classification " COVID-19 AI Classification") repository from the [Peter Moss COVID-19 AI Research](https://github.com/COVID-19-AI-Research-Project "Peter Moss COVID-19 AI Research") Github Organization.

To clone the repository and install the COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4, make sure you have Git installed. Now navigate to the home directory on your device using terminal/commandline, and then use the following command.

```
$ git clone https://github.com/COVID-19-AI-Research-Project/AI-Classification.git
```

Once you have used the command above you will see a directory called **COVID-19-AI-Research-Project** in your home directory.

```
ls
```

Using the ls command in your home directory should show you the following.

```
COVID-19-AI-Research-Project
```

Navigate to **COVID-19-AI-Research-Project/Projects/3** directory, this is your project root directory for this tutorial.

### Developer Forks

Developers from the Github community that would like to contribute to the development of this project should first create a fork, and clone that repository. For detailed information please view the [CONTRIBUTING](../../../../CONTRIBUTING.md "CONTRIBUTING") guide. You should pull the latest code from the development branch.

```
  $ git clone -b "0.3.0" https://github.com/COVID-19-AI-Research-Project/AI-Classification.git
```

The **-b "0.3.0"** parameter ensures you get the code from the latest master branch. Before using the below command please check our latest master branch in the button at the top of the project README.

&nbsp;

# Installation

Use the following commands to install the required software.

## Configuration

You will find the configuration file in the project 2 root directory.

```
{
  "data": {
      "allowed": [
          ".png"
      ],
      "batch": 64,
      "channels": 3,
      "dim": 64,
      "test_0": [
          "Model/Data/0/Non-Covid (1).png",
          "Model/Data/0/Non-Covid (54).png",
          "Model/Data/0/Non-Covid (104).png",
          "Model/Data/0/Non-Covid (389).png",
          "Model/Data/0/Non-Covid (582).png"
      ],
      "test_1": [
          "Model/Data/1/Covid (10).png",
          "Model/Data/1/Covid (76).png",
          "Model/Data/1/Covid (156).png",
          "Model/Data/1/Covid (356).png",
          "Model/Data/1/Covid (675).png"
      ],
      "threshold": 0.5,
      "train": "Model/Data"
  },
  "iotJumpWay": {
      "host": "",
      "port": 8883,
      "loc": 0,
      "zne": 0,
      "id": 0,
      "key": "",
      "name": "",
      "mqtt": {
          "username": "",
          "password": ""
      }
  },
  "model": {
      "json": "Model/model.json",
      "labels": [
          0,
          1
      ],
      "weights": "Model/model.h5"
  },
  "modes": [
      "Classify",
      "Client",
      "Server"
  ],
  "server": {
      "ip": "",
      "port": 8181
  }
}
```

## Easy Install

The following will install all dependencies.

```
sh Scripts/Installation/Shell/Install.sh
```

## Manual Install

The following will install all dependencies. 

```
sudo apt-get update
sudo apt-get upgrade
sudo pip3 install psutil
sudo pip3 install requests
sudo pip3 install numpy
sudo pip3 install jsonpickle
sudo pip3 install flask
sudo pip3 install paho-mqtt
sudo apt-get install gfortran
sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev
sudo apt-get install libatlas-base-dev libopenblas-dev libblas-dev
sudo apt-get install liblapack-dev cython
sudo pip3 install pybind11
sudo pip3 install h5py
wget https://github.com/Qengineering/Tensorflow-Raspberry-Pi/raw/master/tensorflow-2.1.0-cp37-cp37m-linux_armv7l.whl
sudo -H pip3 install tensorflow-2.1.0-cp37-cp37m-linux_armv7l.whl
```

&nbsp;

# Data

Now you need to download the [SARS-COV-2 Ct-Scan Dataset](https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset "SARS-COV-2 Ct-Scan Dataset"). Once you have downloaded the data you need to add the negative samples to the **Model/Data/0/** directory, and the positive samples to the **Model/Data/1/** directory.

## Test Data

In the project configuration file you will find **data->test_0** and **data->test_1**. The files provided will allow you to use the same test data for your real-world testing when using the local classifier and the HTTP classifier.

If you are using the pre-trained model provided, you must use the same images as they are the only unseen images.

These files are skipped during the augmentation process and used when using the local and HTTP classifier. You will also use them in the HIAS UI by sending them to the server for classification.

You can use the exact data we used, or you can change them to any files you like when training Project 2.

## iotJumpWay

This system uses the [HIAS](https://github.com/LeukemiaAiResearch/HIAS "HIAS") iotJumpWay broker to communicate. You should already have followed the [HIAS Installation Guide](https://github.com/LeukemiaAiResearch/HIAS/blob/master/Documentation/Installation/Installation.md "HIAS Installation Guide") and have the server and broker online. 

Once you have accessed your server head to the iotJumpWay devices section. **IoT->Devices** once ther click on the **+** sign to create a new device. Fill out the required details and submit the form. You will be redirected to your device page. 

![HIAS](../../Media/Images/HIAS-Device.png)

You will need to add your HIAS URL to the **iotJumpWay->host** section in the project configs, **port** should be 8883, then add Location ID, Zone ID, Device ID, Device Name and the MQTT username and password. 

### ipinfo

This project sends regular updates to the iotJumpWay which allows the UI to know vital information about the device such as location. For this you need to register a key at [ipinfo.io](https://ipinfo.io "ipinfo.io"). Once you have your key you need to add it to the **iotJumpWay->key** section in the project confs.


&nbsp;

# Continue

Now continue with the [COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4](../../Projects/3/ "COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4") tutorial.

&nbsp;

# Contributing

Peter Moss COVID-19 AI Research Project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking your repositories and submitting your pull requests. You will also find information about your code of conduct on this page.

## Contributors

- [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai/team/adam-milton-barker "Adam Milton-Barker") - [Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss](https://www.leukemiaresearchassociation.ai "Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss") President & Lead Developer, Sabadell, Spain

&nbsp;

# Versioning

You use SemVer for versioning. For the versions available, see [Releases](../../../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

You use the [repo issues](../../../../issues "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](../../../../CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.
