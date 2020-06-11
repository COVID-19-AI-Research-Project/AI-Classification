#!/bin/bash

FMSG="- COVID-19 AI Classification Tensorflow installation terminated"

read -p "? This script will install the COVID-19 AI Classification repository's required Python libraries and Tensorflow on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then

    echo "- Installing required Python libraries and Tensorflow"
    
    pip3 install numpy
    pip3 install scipy
    pip3 install scikit-image
    pip3 install pandas
    pip3 install scikit-learn
    pip3 install matplotlib
    pip3 install jsonpickle
    pip3 install flask
    pip3 install tensorflow-gpu==2.1.0

else
    echo $FMSG;
    exit
fi