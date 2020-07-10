# Peter Moss COVID-19 AI Research Project

## COVID-19 AI Classification

[![COVID-19 AI-Classification](Media/Images/covid-19-ai-classification.png)](https://github.com/COVID-19-AI-Research-Project/AI-Classification)

[![CURRENT VERSION](https://img.shields.io/badge/CURRENT%20VERSION-0.4.0-blue.svg)](https://github.com/COVID-19-AI-Research-Project/AI-Classification/tree/0.4.0) [![CURRENT DEV BRANCH](https://img.shields.io/badge/CURRENT%20DEV%20BRANCH-0.5.0-blue.svg)](https://github.com/COVID-19-AI-Research-Project/AI-Classification/tree/0.5.0)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [DISCLAIMER](#disclaimer)
- [Projects](#projects)
- [Contributing](#contributing)
  - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugs-issues)

&nbsp;

# Introduction

The **Peter Moss COVID-19 AI Research Project AI Classification** repository is a collection of open source Artificial Intelligence for COVID-19 detection/early detection created by our team. The projects in this repository focus on using AI for classifying COVID-19 using computer vision, including Convolutional Neural Networks (CNN) & Generative Adversarial Networks (GAN).

&nbsp;

# DISCLAIMER

These projects should be used for research purposes only. The purpose of the projects are to show the potential of Artificial Intelligence for medical support systems such as diagnosis systems. 

Although the programs are very accurate and show good results both on paper and in real world testing, they are not meant to be an alternative to professional medical diagnosis. 

Developers that have contributed to this repository have experience in using Artificial Intelligence for detecting certain types of cancer & COVID-19. They are not a doctors, medical or cancer/COVID-19 experts. 

Salvatore Raieli is a bioinformatician researcher and PhD in Immunology, but does not work in medical diagnosis. 

Please use these systems responsibly.

&nbsp;

# Projects

Below you will find details of the projects in this repository. Projects with HIAS = YES require an installation of [HIAS](https://github.com/LeukemiaAiResearch/HIAS "HIAS"), you can use this project without HIAS by commenting out the following lines in **COVID19DN.py**:

```
COVID19DN.iotjumpway_client()
COVID19DN.threading()
```

| ID  | Project                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | HIAS | Author                                                                                                        |
| --- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------- |
| 1   | [COVID-19 Pneumonia detection/early detection](Projects/1/ "COVID-19 Pneumonia detection/early detection") | Detects Covid-19 Pneumonia signs from CT Scan Images by a CNN Model. The model have a uniform dataset of 764 Images of CT Scan which consist 349 Images of Covid-19 Pneumonia affected patients and remaining shows normal patient scans.                                                                                                                                                                                                                                                                                                   | NO   | [Aniruddh Sharma](https://www.leukemiaresearchassociation.ai/team/aniruddh-sharma "Aniruddh Sharma")          |
| 2   | [COVID-19 DenseNet](Projects/2/ "COVID-19 DenseNet")                                                       | Uses DenseNet and [SARS-COV-2 Ct-Scan Dataset](https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset "SARS-COV-2 Ct-Scan Dataset"), a large dataset of CT scans for SARS-CoV-2 (COVID-19) identification created by our collaborators, Plamenlancaster: [Professor Plamen Angelov](https://www.lancaster.ac.uk/lira/people/#d.en.397371) from [Lancaster University](https://www.lancaster.ac.uk/)/ Centre Director @ [Lira](https://www.lancaster.ac.uk/lira/), & his researcher, [Eduardo Soares PhD](https://www.lancaster.ac.uk/sci-tech/about-us/people/eduardo-almeida-soares). | YES  | [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai/team/adam-milton-barker "Adam Milton-Barker") |
| 3   | [COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4](Projects/3/ "COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4")                                                       | This project uses the trained model from Project 2 and has been modfied to work on a Raspberry Pi 4. You can either train your own model using [Project 2](Projects/2/ "Project 2") or you can use the pre-trained model provided. | YES  | [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai/team/adam-milton-barker "Adam Milton-Barker") |
| 4   | [COVID-19 FastAI Classifiers](Projects/4/ "COVID-19 FastAI Classifiers")                                                       |This project provides notebooks and tutorials for creating  Convolutional Neural Network models for detecting COVID-19 in CT-Scans with FastAI. | NO  | [Salvatore Raieli](https://www.leukemiaresearchassociation.ai/team/salvatore-raieli  "Salvatore Raieli") |

&nbsp;

# Contributing

The Peter Moss COVID-19 AI Research Project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull requests. You will also find information about our code of conduct on this page.

## Contributors

- [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai/team/adam-milton-barker "Adam Milton-Barker") - [Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss](https://www.leukemiaresearchassociation.ai "Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss") President & Lead Developer, Sabadell, Spain

- [Aniruddh Sharma](https://www.leukemiaresearchassociation.ai/team/aniruddh-sharma "Aniruddh Sharma") - [Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss](https://www.leukemiaresearchassociation.ai "Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss") R&D, Ahmedabad, India

- [Salvatore Raieli](https://www.leukemiaresearchassociation.ai/team/salvatore-raieli  "Salvatore Raieli") - [Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss](https://www.leukemiaresearchassociation.ai "Asociacion De Investigation En Inteligencia Artificial Para La Leucemia Peter Moss") Bioinformatics & Immunology AI R&D, Bologna, Italy

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](issues "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.
