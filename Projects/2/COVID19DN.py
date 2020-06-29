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
# Last Modified: 2020-06-28
#
############################################################################################

import psutil, requests, sys, threading

from threading import Thread

from Classes.Helpers import Helpers
from Classes.Data import Data
from Classes.iotJumpWay import Device as iotJumpWay
from Classes.Model import Model
from Classes.Server import Server


class COVID19DN():
    """ COVID19DN Class

    Core COVID-19 Tensorflow DenseNet Classifier wrapper class using Tensroflow 2.
    """

    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("Core")

        self.Helpers.logger.info(
            "COVID-19 Tensorflow DenseNet Classifier initialization complete.")
        
    def iotjumpway_client(self):
        """ Starts iotJumpWay Client. """

        # Initiates the iotJumpWay connection class
        self.iotJumpWayDevice = iotJumpWay({
            "host": self.Helpers.confs["iotJumpWay"]["host"],
            "port": self.Helpers.confs["iotJumpWay"]["port"],
            "lid": self.Helpers.confs["iotJumpWay"]["loc"],
            "zid": self.Helpers.confs["iotJumpWay"]["zne"],
            "did": self.Helpers.confs["iotJumpWay"]["id"],
            "dn": self.Helpers.confs["iotJumpWay"]["name"],
            "un": self.Helpers.confs["iotJumpWay"]["mqtt"]["username"],
            "pw": self.Helpers.confs["iotJumpWay"]["mqtt"]["password"]
        })
        self.iotJumpWayDevice.connect()
            
    def life(self):
        """ Sends vital statistics to HIAS """
        
        # Get device vitals
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory()[2]
        hdd = psutil.disk_usage('/').percent
        tmp = psutil.sensors_temperatures()['coretemp'][0].current
        r = requests.get('http://ipinfo.io/json?token=' + self.Helpers.confs["iotJumpWay"]["key"])
        data = r.json()
        location = data["loc"].split(',')
  
        # Log device vitals
        self.Helpers.logger.info("COVID19DN Life (TEMPERATURE): " + str(tmp) + "\u00b0")
        self.Helpers.logger.info("COVID19DN Life (CPU): " + str(cpu) + "%")
        self.Helpers.logger.info("COVID19DN Life (Memory): " + str(mem) + "%")
        self.Helpers.logger.info("COVID19DN Life (HDD): " + str(hdd) + "%")
        self.Helpers.logger.info("COVID19DN Life (LAT): " + str(location[0]))
        self.Helpers.logger.info("COVID19DN Life (LNG): " + str(location[1]))
        
        # Send iotJumpWay notification
        self.iotJumpWayDevice.devicePub("Life", {
            "CPU": cpu,
            "Memory": mem,
            "Diskspace": hdd,
            "Temperature": tmp,
            "Latitude": location[0],
            "Longitude": location[1]
        })
        
        threading.Timer(60.0, self.life).start()
        
    def threading(self):
        """ Creates required module threads. """
        
        # Life thread
        Thread(target = self.life, args = ()).start()
        threading.Timer(60.0, self.life).start()

    def do_data(self):
        """ Sorts the training data. """

        # Load the data class
        self.Data = Data()
        # Process the data
        self.Data.process_data(
            self.Data.paths_n_labels())

    def do_train(self):
        """ Creates & trains the model. """
        
        # Load the model class
        self.Model = Model()
        # Create the model
        self.Model.do_model(self.Data)
        # Train the model
        self.Model.do_train()
        # Validate the model
        self.Model.do_evaluate()

    def do_load_model(self):
        """ Loads the model """

        # Load the model and weights
        self.Model.load_model_and_weights()

    def do_classify(self):
        """ Loads model and classifies test data """

        # Load the model class
        self.Model = Model()
        # Load the model
        self.do_load_model()
        # Classify the test data
        self.Model.test_classifier()

    def do_server(self):
        """ Loads the API server """

        # Load the model class
        self.Model = Model()
        # Load the model
        self.do_load_model()
        # Load the server class
        self.Server = Server(self.Model)
        # Start the server
        self.Server.start()

    def do_http_classify(self):
        """ Loads model and classifies test data """

        # Load the model class
        self.Model = Model()
        # Classify the test data via the server
        self.Model.test_http_classifier()

COVID19DN = COVID19DN()

def main():

    if len(sys.argv) < 2:
        COVID19DN.Helpers.logger.info(
            "You must provide an argument! Server, Train or Classify")
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
        COVID19DN.iotjumpway_client()
        COVID19DN.threading()
        COVID19DN.do_server()

    elif mode == "Client":
        """ Runs the classifier in client mode. """
        COVID19DN.do_http_classify()

if __name__ == "__main__":
    main()