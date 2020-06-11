############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    AI-Classification
# Repo Project:  COVID-19 Tensorflow DenseNet Classifier
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         Data Class
# Description:   Data functions for the COVID-19 Tensorflow DenseNet Classifier.
# License:       MIT License
# Last Modified: 2020-06-10
#
############################################################################################

import cv2
import random
import os

import numpy as np
import pandas as pd
import tensorflow as tf

from numpy.random import seed

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

from Classes.Helpers import Helpers
from Classes.Augmentation import Augmentation


class Data():
    """ Data Class

    Data functions for the COVID-19 Tensorflow DenseNet Classifier.
    """

    def __init__(self):
        """ Initializes the Data Class. """

        self.Helpers = Helpers("Data", False)

        self.dim = self.Helpers.confs["data"]["dim"]
        self.seed = self.Helpers.confs["data"]["seed"]
        self.tdir = self.Helpers.confs["data"]["train"]

        seed(self.seed)
        random.seed(self.seed)

        self.data = []
        self.labels = []

        self.Helpers.logger.info("Data class initialization complete.")

    def paths_n_labels(self):
        """ Stores data paths and labels as a list of tuples. """

        rdata = []

        for ddir in os.listdir(self.tdir):
            tpath = os.path.join(self.tdir, ddir)
            if os.path.isdir(tpath):
                for filename in os.listdir(tpath):
                    if filename.lower().endswith(tuple(self.Helpers.confs["data"]["allowed"])):
                        rdata.append(
                            (os.path.join(tpath, filename), ddir))
                    else:
                        continue

        df = pd.DataFrame(rdata, columns=['img', 'lbl'], index=None)
        df = df.sample(frac=1.).reset_index(drop=True)

        self.Helpers.logger.info("Data Paths: " + str(len(rdata)))

        return df

    def process_data(self, df):
        """ Processes the data. """

        count = 0
        neg_count = 0
        pos_count = 0

        dl = len(df)

        self.data = np.zeros(
            (dl * 9, self.dim, self.dim, 3), dtype=np.float32)
        self.labels = np.zeros(
            (dl * 9, 2), dtype=np.float32)

        aug = Augmentation()

        for d in range(0, dl):

            img = df.iloc[d]['img']

            if img in self.Helpers.confs["data"]["test_0"] or img in self.Helpers.confs["data"]["test_1"]:
                self.Helpers.logger.info("Skipping Test Image: " + img)
                continue

            self.Helpers.logger.info("Augmenting Train Image: " + img)

            image = self.resize(img, self.dim)
            label = df.iloc[d]['lbl']
            
            print(label)

            if image.shape[2] == 1:
                image = np.dstack([image, image, image])

            self.data[count] = image.astype(np.float32)/255.
            self.labels[count] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            self.data[count+1] = aug.grayscale(image)
            self.labels[count+1] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            self.data[count+2] = aug.equalize_hist(image)
            self.labels[count+2] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            horizontal, vertical = aug.reflection(image)

            self.data[count+3] = horizontal
            self.labels[count+3] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            self.data[count+4] = vertical
            self.labels[count+4] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            self.data[count+5] = aug.gaussian(image)
            self.labels[count+5] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            self.data[count+6] = aug.translate(image)
            self.labels[count+6] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            self.data[count+7] = aug.shear(image)
            self.labels[count+7] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            self.data[count+8] = aug.rotation(image)
            self.labels[count+8] = tf.keras.utils.to_categorical(
                label, num_classes=2)

            if label == 0:
                neg_count += 9
            else:
                pos_count += 9
            count += 9

        self.pshuffle()
        self.convert_data()

        self.Helpers.logger.info("Raw data: " + str(count))
        self.Helpers.logger.info("Raw negative data: " + str(neg_count))
        self.Helpers.logger.info("Raw positive data: " + str(count))
        self.Helpers.logger.info("Augmented data: " + str(self.data.shape))
        self.Helpers.logger.info("Labels: " + str(self.labels.shape))

        self.get_split()

    def convert_data(self):
        """ Converts the training data to a numpy array. """

        self.data = np.array(self.data)
        self.Helpers.logger.info("Data shape: " + str(self.data.shape))

    def pshuffle(self):
        """ Shuffles the data and labels. """

        self.data, self.labels = shuffle(
            self.data, self.labels, random_state=self.seed)

    def get_split(self):
        """ Splits the data and labels creating training and validation datasets. """

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.data, self.labels, test_size=self.Helpers.confs["data"]["test_size"], random_state=self.seed)

        self.Helpers.logger.info("Training data: " + str(self.X_train.shape))
        self.Helpers.logger.info("Training labels: " + str(self.y_train.shape))
        self.Helpers.logger.info("Validation data: " + str(self.X_test.shape))
        self.Helpers.logger.info(
            "Validation labels: " + str(self.y_test.shape))

    def resize(self, path, dim):
        """ Resizes an image to the provided dimensions (dim). """

        return cv2.resize(cv2.imread(path), (dim, dim), interpolation=cv2.INTER_AREA)
