############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    AI-Classification
# Repo Project:  COVID-19 Tensorflow DenseNet Classifier
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         Model Class
# Description:   Model functions for the COVID-19 Tensorflow DenseNet Classifier.
# License:       MIT License
# Last Modified: 2020-06-10
#
############################################################################################

import cv2
import json
import requests
import time

import tensorflow as tf

import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import confusion_matrix

from Classes.Helpers import Helpers


class Model():
    """ Model Class

    Model functions for the COVID-19 Tensorflow DenseNet Classifier.
    """

    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("Model", False)

    def do_model(self, data):

        self.Data = data

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

    def do_train(self):
        """ Trains the network. """

        self.Helpers.logger.info("Using Adam Optimizer.")

        optimizer = tf.keras.optimizers.Adam(lr=self.Helpers.confs["model"]["lr"],
                                             beta_1=self.Helpers.confs["model"]["beta_1"],
                                             beta_2=self.Helpers.confs["model"]["beta_2"],
                                             epsilon=self.Helpers.confs["model"]["epsilon"],
                                             decay=self.Helpers.confs["model"]["decay"])

        self.tfmodel.compile(loss='categorical_crossentropy',
                             optimizer=optimizer, metrics=[tf.keras.metrics.BinaryAccuracy(name='acc'),
                                                           tf.keras.metrics.Precision(
                                 name='precision'),
                                 tf.keras.metrics.Recall(
                                 name='recall'),
                                 tf.keras.metrics.AUC(name='auc')])

        monitor = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_acc',
                                                       factor=self.Helpers.confs["model"]["factor"],
                                                       patience=self.Helpers.confs["model"]["patience"],
                                                       verbose=1,
                                                       min_lr=self.Helpers.confs["model"]["min_lr"])

        checkpoint = tf.keras.callbacks.ModelCheckpoint(
            self.Helpers.confs["model"]["weights"], verbose=1, save_best_only=True)

        self.history = self.tfmodel.fit(self.Data.X_train, self.Data.y_train,
                                        batch_size=self.Helpers.confs["data"]["batch"],
                                        epochs=self.Helpers.confs["model"]["epochs"],
                                        callbacks=[monitor, checkpoint],
                                        validation_data=(self.Data.X_test, self.Data.y_test))

        print(self.history)
        print("")

        self.save_model_as_json()

    def do_evaluate(self):
        """ Evaluates the model """

        self.do_predictions()

        metrics = self.tfmodel.evaluate(
            self.Data.X_test, self.Data.y_test, verbose=0)
        for name, value in zip(self.tfmodel.metrics_names, metrics):
            self.Helpers.logger.info("Metrics: " + name + " " + str(value))
        print()

        self.visualize_metrics()
        self.confusion_matrix()
        self.figures_of_merit()

    def do_predictions(self):
        """ Makes predictions on the train & test sets. """

        self.train_preds = self.tfmodel.predict(self.Data.X_train)
        self.test_preds = self.tfmodel.predict(self.Data.X_test)

        self.Helpers.logger.info(
            "Training predictions: " + str(self.train_preds))
        self.Helpers.logger.info(
            "Testing predictions: " + str(self.test_preds))
        print("")

    def visualize_metrics(self):
        """ Visualize the metrics. """

        plt.plot(self.history.history['acc'])
        plt.plot(self.history.history['val_acc'])
        plt.title('Model Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.ylim((0, 1))
        plt.legend(['Train', 'Validate'], loc='upper left')
        plt.savefig('Model/Plots/Accuracy.png')
        plt.show()
        plt.clf()

        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.title('Model Loss')
        plt.ylabel('loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validate'], loc='upper left')
        plt.savefig('Model/Plots/Loss.png')
        plt.show()
        plt.clf()

        plt.plot(self.history.history['auc'])
        plt.plot(self.history.history['val_auc'])
        plt.title('Model AUC')
        plt.ylabel('AUC')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validate'], loc='upper left')
        plt.savefig('Model/Plots/AUC.png')
        plt.show()
        plt.clf()

        plt.plot(self.history.history['precision'])
        plt.plot(self.history.history['val_precision'])
        plt.title('Model Precision')
        plt.ylabel('Precision')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validate'], loc='upper left')
        plt.savefig('Model/Plots/Precision.png')
        plt.show()
        plt.clf()

        plt.plot(self.history.history['recall'])
        plt.plot(self.history.history['val_recall'])
        plt.title('Model Recall')
        plt.ylabel('Recall')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validate'], loc='upper left')
        plt.savefig('Model/Plots/Recall.png')
        plt.show()
        plt.clf()

    def confusion_matrix(self):
        """ Prints/displays the confusion matrix. """

        self.matrix = confusion_matrix(self.Data.y_test.argmax(axis=1),
                                       self.test_preds.argmax(axis=1))

        self.Helpers.logger.info("Confusion Matrix: " + str(self.matrix))
        print("")

        plt.imshow(self.matrix, cmap=plt.cm.Blues)
        plt.xlabel("Predicted labels")
        plt.ylabel("True labels")
        plt.xticks([], [])
        plt.yticks([], [])
        plt.title('Confusion matrix ')
        plt.colorbar()
        plt.savefig('Model/Plots/Confusion-Matrix.png')
        plt.show()
        plt.clf()

    def figures_of_merit(self):
        """ Calculates/prints the figures of merit. """

        test_len = len(self.Data.X_test)

        TP = self.matrix[1][1]
        TN = self.matrix[0][0]
        FP = self.matrix[0][1]
        FN = self.matrix[1][0]

        TPP = (TP * 100)/test_len
        FPP = (FP * 100)/test_len
        FNP = (FN * 100)/test_len
        TNP = (TN * 100)/test_len

        specificity = TN/(TN+FP)

        misc = FP + FN
        miscp = (misc * 100)/test_len

        self.Helpers.logger.info(
            "True Positives: " + str(TP) + "(" + str(TPP) + "%)")
        self.Helpers.logger.info(
            "False Positives: " + str(FP) + "(" + str(FPP) + "%)")
        self.Helpers.logger.info(
            "True Negatives: " + str(TN) + "(" + str(TNP) + "%)")
        self.Helpers.logger.info(
            "False Negatives: " + str(FN) + "(" + str(FNP) + "%)")

        self.Helpers.logger.info("Specificity: " + str(specificity))
        self.Helpers.logger.info(
            "Misclassification: " + str(misc) + "(" + str(miscp) + "%)")

    def save_model_as_json(self):
        """ Saves the model to JSON. """

        with open(self.Helpers.confs["model"]["json"], "w") as file:
            file.write(self.tfmodel.to_json())

        self.Helpers.logger.info(
            "Model JSON saved " + self.Helpers.confs["model"]["json"])

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
            self.Helpers.logger.info("Predicted Label: " + str(prediction))

            msg = ""
            if prediction == 1 and testFile.find("/1/") != -1:
                tp += 1
                msg = "COVID-19 correctly detected (True Positive)"
            elif prediction == 1 and testFile.find("/0/") != -1:
                fp += 1
                msg = "COVID-19 incorrectly detected (False Positive)"
            elif prediction == 0 and testFile.find("/0/") != -1:
                tn += 1
                msg = "COVID-19 correctly not detected (True Negative)"
            elif prediction == 0 and testFile.find("/1/") != -1:
                fn += 1
                msg = "COVID-19 incorrectly not detected (False Negative)"

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
            if response["Classification"] == 1 and testFile.find("/1/") != -1:
                tp += 1
                msg = "COVID-19 correctly detected (True Positive)"
            elif response["Classification"] == 1 and testFile.find("/0/") != -1:
                fp += 1
                msg = "COVID-19 incorrectly detected (False Positive)"
            elif response["Classification"] == 0 and testFile.find("/0/") != -1:
                tn += 1
                msg = "COVID-19 correctly not detected (True Negative)"
            elif response["Classification"] == 0 and testFile.find("/1/") != -1:
                fn += 1
                msg = "COVID-19 incorrectly not detected (False Negative)"

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
        x = np.expand_dims(x, axis=0)
        x /= 255

        predictions = self.tfmodel.predict(x)
        prediction = predictions[0]
        prediction = np.argmax(prediction)

        return prediction
