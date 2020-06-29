#!/bin/bash

FMSG="- COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4 installation terminated"

read -p "? This script will install the COVID-19 Tensorflow DenseNet Classifier For Raspberry Pi 4 required Python libraries and Tensorflow on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then

    echo "- Installing required Python libraries and Tensorflow"
    
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

else
    echo $FMSG;
    exit
fi