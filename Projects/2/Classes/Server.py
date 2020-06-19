############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    AI-Classification
# Repo Project:  COVID-19 Tensorflow DenseNet Classifier
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         Server Class
# Description:   Server functions for the COVID-19 Tensorflow DenseNet Classifier.
# License:       MIT License
# Last Modified: 2020-06-10
#
############################################################################################

import jsonpickle

import numpy as np

from flask import Flask, request, Response

from Classes.Helpers import Helpers


class Server():
    """ Server helper class

    Server functions for the COVID-19 Tensorflow DenseNet Classifier.
    """

    def __init__(self, model):
        """ Initializes the class. """

        self.Helpers = Helpers("Server", False)

        self.model = model

    def start(self):
        """ Starts the server. """

        app = Flask(__name__)

        @app.route('/Inference', methods=['POST'])
        def Inference():
            """ Responds to standard HTTP request. """

            message = ""
            classification, confidence = self.model.http_classify(request)

            if classification == 1:
                message = "COVID-19 detected!"
                diagnosis = "Positive"
            elif classification == 0:
                message = "COVID-19 not detected!"
                diagnosis = "Negative"

            resp = jsonpickle.encode({
                'Response': 'OK',
                'Message': message,
                'Diagnosis': diagnosis,
                'Confidence': np.asscalar(confidence)
            })
            
            return Response(response=resp, status=200, mimetype="application/json")

        app.run(host=self.Helpers.confs["server"]["ip"],
                port=self.Helpers.confs["server"]["port"])
