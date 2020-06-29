############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    AI-Classification
# Repo Project:  COVID-19 Tensorflow DenseNet Classifier
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         Model Class
# Description:   Model functions for the COVID-19 Tensorflow DenseNet Classifier for the
#                Raspberry Pi 4.
# License:       MIT License
# Last Modified: 2020-06-29
#
############################################################################################

import cv2, json, requests, time

import tensorflow as tf

import numpy as np

from Classes.Helpers import Helpers


class Model():
    """ Model Class

    Model functions for the COVID-19 Tensorflow DenseNet Classifier.
    """

    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("Model", False)

    def do_model(self):

        inp = tf.keras.Input(shape=(self.Helpers.confs["data"]["dim"], self.Helpers.confs["data"]["dim"],
                                    self.Helpers.confs["data"]["channels"]))

        net = tf.keras.layers.Conv2D(3, (3, 3), padding='same')(inp)

        dnet = tf.keras.applications.DenseNet121(
            weights='imagenet', include_top=False)
        net = dnet(net)

        net = tf.keras.layers.GlobalAveragePooling2D()(net)
        net = tf.keras.layers.BatchNormalization()(net)
        net = tf.keras.layers.Dropout(
            self.Helpers.confs["model"]["dropout"])(net)
        net = tf.keras.layers.Dense(256, activation='relu')(net)
        net = tf.keras.layers.BatchNormalization()(net)
        net = tf.keras.layers.Dropout(
            self.Helpers.confs["model"]["dropout"])(net)

        preds = tf.keras.layers.Dense(
            2, activation='softmax', name='root')(net)

        self.tfmodel = tf.keras.Model(inp, preds)
        self.tfmodel.summary()

        self.Helpers.logger.info("Network initialization complete.")

    def load_model_and_weights(self):
        """ Loads the model and weights. """

        with open(self.Helpers.confs["model"]["json"]) as file:
            m_json = file.read()

        self.tfmodel = tf.keras.models.model_from_json(m_json)
        self.tfmodel.load_weights(self.Helpers.confs["model"]["weights"])

        self.Helpers.logger.info("Model loaded ")

        self.tfmodel.summary()
        print("")

    def test_classifier(self):
        """ Tests the trained model. """

        files = 0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        combined = self.Helpers.confs["data"]["test_0"] + \
            self.Helpers.confs["data"]["test_1"]

        for testFile in combined:

            files += 1

            img = tf.keras.preprocessing.image.load_img(testFile, grayscale=False,
                                                        target_size=(self.Helpers.confs["data"]["dim"],
                                                                     self.Helpers.confs["data"]["dim"]))
            self.Helpers.logger.info("Loaded test image " + testFile)

            prediction = self.get_prediction(img)
            self.Helpers.logger.info("Predicted Label: " + str(prediction[0]))

            msg = ""
            if prediction[0] == 1 and testFile.find("/1/") != -1:
                tp += 1
                msg = "COVID-19 correctly detected (True Positive) with confidence: " + str(
                    prediction[1])
            elif prediction[0] == 1 and testFile.find("/0/") != -1:
                fp += 1
                msg = "COVID-19 incorrectly detected (False Positive) with confidence: " + str(
                    prediction[1])
            elif prediction[0] == 0 and testFile.find("/0/") != -1:
                tn += 1
                msg = "COVID-19 correctly not detected (True Negative) with confidence: " + str(
                    prediction[1])
            elif prediction[0] == 0 and testFile.find("/1/") != -1:
                fn += 1
                msg = "COVID-19 incorrectly not detected (False Negative) with confidence: " + str(
                    prediction[1])

            self.Helpers.logger.info(msg)

        self.Helpers.logger.info("Images Classified: " + str(files))
        self.Helpers.logger.info("True Positives: " + str(tp))
        self.Helpers.logger.info("False Positives: " + str(fp))
        self.Helpers.logger.info("True Negatives: " + str(tn))
        self.Helpers.logger.info("False Negatives: " + str(fn))

    def test_http_classifier(self):
        """ Tests the trained model. """

        files = 0
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        combined = self.Helpers.confs["data"]["test_0"] + \
            self.Helpers.confs["data"]["test_1"]

        for testFile in combined:

            files += 1

            response = self.send_request(testFile)

            msg = ""
            if response["Diagnosis"] == "Positive" and testFile.find("/1/") != -1:
                tp += 1
                msg = "COVID-19 correctly detected (True Positive) with confidence: " + str(
                    response["Confidence"])
            elif response["Diagnosis"] == "Positive" and testFile.find("/0/") != -1:
                fp += 1
                msg = "COVID-19 incorrectly detected (False Positive) with confidence: " + str(
                    response["Confidence"])
            elif response["Diagnosis"] == "Negative" and testFile.find("/0/") != -1:
                tn += 1
                msg = "COVID-19 correctly not detected (True Negative) with confidence: " + str(
                    response["Confidence"])
            elif response["Diagnosis"] == "Negative" and testFile.find("/1/") != -1:
                fn += 1
                msg = "COVID-19 incorrectly not detected (False Negative) with confidence: " + str(
                    response["Confidence"])

            self.Helpers.logger.info(msg)
            print()
            time.sleep(7)

        self.Helpers.logger.info("Images Classifier: " + str(files))
        self.Helpers.logger.info("True Positives: " + str(tp))
        self.Helpers.logger.info("False Positives: " + str(fp))
        self.Helpers.logger.info("True Negatives: " + str(tn))
        self.Helpers.logger.info("False Negatives: " + str(fn))

    def send_request(self, img_path):
        """ Sends image to the inference API endpoint. """

        addr = "http://" + self.Helpers.confs["server"]["ip"] + \
            ':'+str(self.Helpers.confs["server"]["port"]) + '/Inference'
        headers = {'content-type': 'image/jpeg'}

        self.Helpers.logger.info("Sending request for: " + img_path)

        _, img_encoded = cv2.imencode('.png', cv2.imread(img_path))
        response = requests.post(
            addr, data=img_encoded.tostring(), headers=headers)
        response = json.loads(response.text)

        return response

    def http_classify(self, req):
        """ Classifies an image sent via HTTP. """

        if len(req.files) != 0:
            img = np.fromstring(req.files['file'].read(), np.uint8)
        else:
            img = np.fromstring(req.data, np.uint8)

        img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (self.Helpers.confs["data"]["dim"],
                               self.Helpers.confs["data"]["dim"]))

        return self.get_prediction(img)

    def get_prediction(self, img):
        """ Gets a prediction for an image. """

        x = tf.keras.preprocessing.image.img_to_array(img)
        x = cv2.cvtColor(x, cv2.COLOR_BGRA2BGR)
        x = np.expand_dims(x, axis=0)
        x /= 255

        predictions = self.tfmodel.predict(x)
        prediction = predictions[0]
        predictioni = np.argmax(prediction)
        prediction = self.Helpers.confs["model"]["labels"][predictioni]
        confidence = predictions[0][prediction]

        return prediction, confidence
