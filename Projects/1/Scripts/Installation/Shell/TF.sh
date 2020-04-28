#!/bin/bash

FMSG="- Python libraries and Tensorflow installation terminated"

read -p "? This script will install the COVID-19 AI Classification's required Python libraries and Tensorflow on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then

    echo "- GeniSysAI installing Python libraries and Tensorflow"

    pip install numpy
    pip install pickle-mixin
    pip install os-sys
    pip install times
    pip install h5py
    pip install random2
    pip install tensorboard==2.1.0
    pip install tensorflow==2.1.0
    pip install tensorflow-gpu==2.1.0

    exit 0

else
    echo $FMSG;
    exit 1
fi