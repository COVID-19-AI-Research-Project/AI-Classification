# Peter Moss COVID-19 AI Research Project

## COVID-19 AI Classification

![GeniSysAI Server](../../../../Media/Images/covid-19-ai-classification.png)

&nbsp;

# Installation & setup

The following guide will take you through setting up and installing the [AI-Classification](https://github.com/COVID-19-AI-Research-Project/AI-Classification/tree/master/Projects/1).

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

# Clone the repository

Clone the [AI-Classification](https://github.com/COVID-19-AI-Research-Project/AI-Classification "AI-Classification") repository from the [Peter Moss Acute Myeloid & Lymphoblastic COVID-19 AI Research Project](https://github.com/COVID-19-AI-Research-Project "Peter Moss COVID-19 AI Research Project") Github Organization.

To clone the repository and install the COVID19 AI Quantum Tensorflow repository, make sure you have Git installed. Now navigate to the location you want to clone the repository to on your device using terminal/commandline, and then use the following command.

The **-b "0.1.0"** parameter ensures you get the code from the latest development branch. Before using the below command please check our latest development branch in the button at the top of this page.

```
  $ git clone -b "0.1.0" https://github.com/COVID-19-AI-Research-Project/AI-Classification.git
```

Once you have used the command above you will see a directory called **AI-Classification** in the location you chose to clone to. In terminal, navigate to the **AI-Classification** directory, this is your project root directory.

## Developer Forks

Developers from the Github community that would like to contribute to the development of this project should first create a fork, and clone that repository. For detailed information please view the [CONTRIBUTING](https://github.com/COVID-19-AI-Research-Project/COVID19-AI-Quantum-Tensorflow/blob/master/CONTRIBUTING.md "CONTRIBUTING") guide.

## Quick Install

To do a continuous install of above Python Libraries and Tensorflow2 after installing Python3.6, use the following command from the [Projects/1](https://github.com/aniruddh-1/AI-Classification/tree/0.1.0/Projects/1):

```
sh Scripts/Installation/Shell/Install.sh
```

&nbsp;

# Contributing

The Peter Moss Acute Myeloid & Lymphoblastic Leukemia AI Research project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull requests. You will also find information about our code of conduct on this page.

## Contributors

- [Aniruddh Sharma](https://www.leukemiaresearchassociation.ai/team/aniruddh-sharma "Aniruddh Sharma") - [Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss](https://www.leukemiaresearchassociation.ai "Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss") R&D, Ahmedabad, India

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](../../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](Media/Images/repo-issues.png "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.
