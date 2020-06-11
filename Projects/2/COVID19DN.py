############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    AI-Classification
# Repo Project:  COVID-19 Tensorflow DenseNet Classifier
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         COVID19DN Class
# Description:   Core COVID-19 Tensorflow DenseNet Classifier wrapper class using Tensroflow 2.
# License:       MIT License
# Last Modified: 2020-06-10
#
############################################################################################

import sys

from Classes.Helpers import Helpers
from Classes.Data import Data
from Classes.Model import Model
from Classes.Server import Server


class COVID19DN():
    """ COVID19DN Class

    Core COVID-19 Tensorflow DenseNet Classifier wrapper class using Tensroflow 2.
    """

    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("Core")

        self.Model = Model()

        self.Helpers.logger.info(
            "COVID19DN Tensorflow initialization complete.")

    def do_data(self):
        """ Sorts the training data. """

        self.Data = Data()
        self.Data.process_data(
            self.Data.paths_n_labels())

    def do_train(self):
        """ Creates & trains the model. """

        self.Model.do_model(self.Data)
        self.Model.do_train()
        self.Model.do_evaluate()

    def do_load_model(self):
        """ Loads the model """

        self.Model.load_model_and_weights()

    def do_classify(self):
        """ Loads model and classifies test data """

        self.do_load_model()
        self.Model.test_classifier()

    def do_server(self):
        """ Loads the API server """

        self.do_load_model()
        self.Server = Server(self.Model)
        self.Server.start()

    def do_http_classify(self):
        """ Loads model and classifies test data """

        self.Model.test_http_classifier()


COVID19DN = COVID19DN()


def main():

    if len(sys.argv) < 2:
        COVID19DN.Helpers.logger.info(
            "You must provide an argument!  Server, Train or Classify")
        exit()
    elif sys.argv[1] not in COVID19DN.Helpers.confs["modes"]:
        COVID19DN.Helpers.logger.info(
            "Mode not supported! Server, Train or Classify")
        exit()

    mode = sys.argv[1]

    if mode == "Train":
        """ Creates and trains the classifier """
        COVID19DN.do_data()
        COVID19DN.do_train()

    elif mode == "Classify":
        """ Runs the classifier locally."""
        COVID19DN.do_classify()

    elif mode == "Server":
        """ Runs the classifier in server mode."""
        COVID19DN.do_server()

    elif mode == "Client":
        """ Runs the classifier in client mode. """
        COVID19DN.do_http_classify()


if __name__ == "__main__":
    main()
