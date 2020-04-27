#!/bin/bash

FMSG="- COVID-19 AI Classification Tensorflow installation terminated"

read -p "? This script will install the COVID-19 AI Classification's required Python libraries and Tensorflow on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then

    echo "- Installing required Python libraries and Tensorflow"

    sh Scripts/Installation/Shell/TF.sh
    if [ $? -ne 0 ]; then
        echo $FMSG;
        exit
    fi

else
    echo $FMSG;
    exit
fi