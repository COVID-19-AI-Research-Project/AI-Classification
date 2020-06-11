############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    AI-Classification
# Repo Project:  COVID-19 Tensorflow DenseNet Classifier
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         Augmentation Class
# Description:   Augmentation functions for the COVID-19 Tensorflow DenseNet Classifier.
# License:       MIT License
# Last Modified: 2020-06-10
#
############################################################################################

import cv2
import random

import numpy as np

from numpy.random import seed
from scipy import ndimage
from skimage import transform as tm

from numpy.random import seed

from Classes.Helpers import Helpers


class Augmentation():
    """ Augmentation Class

    Augmentation functions for the COVID-19 Tensorflow DenseNet Classifier.
    """

    def __init__(self):
        """ Initializes the Augmentation Class. """

        self.Helpers = Helpers("Augmentation", False)

        self.seed = self.Helpers.confs["data"]["seed"]
        seed(self.seed)

        self.Helpers.logger.info("Augmentation class initialization complete.")

    def grayscale(self, data):
        """ Creates a grayscale copy. """

        gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        return np.dstack([gray, gray, gray]).astype(np.float32)/255.

    def equalize_hist(self, data):
        """ Creates a histogram equalized copy. 

        Credit: Amita Kapoor & Taru Jain
        Exploring novel convolutional network architecture to build a classification 
        system for better assistance in diagonosing Acute Lymphoblastic Leukemia in 
        blood cells.
        https://github.com/AMLResearchProject/ALL-Keras-2019
        """

        img_to_yuv = cv2.cvtColor(data, cv2.COLOR_BGR2YUV)
        img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
        hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
        return hist_equalization_result.astype(np.float32)/255.

    def reflection(self, data):
        """ Creates a reflected copy. """

        return cv2.flip(data, 0).astype(np.float32)/255., cv2.flip(data, 1).astype(np.float32)/255.

    def gaussian(self, data):
        """ Creates a gaussian blurred copy. """

        return ndimage.gaussian_filter(data, sigma=5.11).astype(np.float32)/255.

    def translate(self, data):
        """ Creates transformed copy. """

        cols, rows, chs = data.shape

        return cv2.warpAffine(data, np.float32([[1, 0, 84], [0, 1, 56]]), (rows, cols),
                              borderMode=cv2.BORDER_CONSTANT, borderValue=(144, 159, 162)).astype(np.float32)/255.

    def rotation(self, data):
        """ Creates rotated copies. """

        cols, rows, chs = data.shape

        random.seed(self.seed)
        rand_deg = random.randint(-180, 180)
        matrix = cv2.getRotationMatrix2D((cols/2, rows/2), rand_deg, 0.70)
        rotated = cv2.warpAffine(data, matrix, (rows, cols), borderMode=cv2.BORDER_CONSTANT,
                                 borderValue=(144, 159, 162))

        rotated = rotated.astype(np.float32)/255.

        return rotated

    def shear(self, data):
        """ Creates a histogram equalized copy. 

        Credit: Amita Kapoor & Taru Jain
        Exploring novel convolutional network architecture to build a classification 
        system for better assistance in diagonosing Acute Lymphoblastic Leukemia in 
        blood cells.
        https://github.com/AMLResearchProject/ALL-Keras-2019
        """

        at = tm.AffineTransform(shear=0.5)
        return tm.warp(data, inverse_map=at)
