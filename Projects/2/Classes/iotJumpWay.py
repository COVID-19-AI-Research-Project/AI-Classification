############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    AI-Classification
# Repo Project:  COVID-19 Tensorflow DenseNet Classifier
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         iotJumpWay Class
# Description:   iotJumpWay functions for the  COVID-19 Tensorflow DenseNet Classifier.
# License:       MIT License
# Last Modified: 2020-06-10
#
############################################################################################

import inspect
import json
import os

import paho.mqtt.client as mqtt

from Classes.Helpers import Helpers


class Device():
    """ iotJumpWay Class

    iotJumpWay functions for the COVID-19 xDNN Python Classifier.
    """

    def __init__(self, configs):
        """ Initializes the class. """

        self.Helpers = Helpers("iotJumpWay")
        self.confs = configs

        self.Helpers.logger.info("Initiating Local iotJumpWay Device.")

        if self.confs['host'] == None:
            raise ConfigurationException("** Host (host) property is required")
        elif self.confs['port'] == None:
            raise ConfigurationException("** Port (port) property is required")
        elif self.confs['lid'] == None:
            raise ConfigurationException(
                "** Location ID (lid) property is required")
        elif self.confs['zid'] == None:
            raise ConfigurationException(
                "** Zone ID (zid) property is required")
        elif self.Helpers.confs["iotJumpWay"]["an"] == None:
        elif self.confs['aid'] == None:
            raise ConfigurationException(
                "** Application ID (aid) property is required")
        elif self.Helpers.confs["iotJumpWay"]["an"] == None:
            raise ConfigurationException(
                "** Application Name (an) property is required")
        elif self.confs['un'] == None:
            raise ConfigurationException(
                "** MQTT UserName (un) property is required")
        elif self.confs['pw'] == None:
            raise ConfigurationException(
                "** MQTT Password (pw) property is required")

        self.mqttClient = None
        self.mqttTLS = "/etc/ssl/certs/DST_Root_CA_X3.pem"

        self.appStatusCallback = None
        self.deviceStatusCallback = None
        self.deviceSensorCallback = None
        self.deviceCommandsCallback = None
        self.deviceNotificationsCallback = None
        self.deviceNotificationsCallback = None

        def __init__(self, configs):

            print("-- Initiating JumpWayMQTT Device")

            self._configs = configs
            self.mqttClient = None
            self.mqttTLS = os.path.dirname(
                os.path.abspath(__file__)) + "/ca.pem"
            self.mqttHost = 'iot.techbubbletechnologies.com'
            self.mqttPort = 8883

            self.deviceStatusCallback = None
            self.deviceCommandsCallback = None
            self.deviceKeysCallback = None
            self.deviceSSLsCallback = None

            if self._configs['locationID'] == None:

                raise ConfigurationException(
                    "** Location ID (locationID) property is required")

            elif self._configs['zoneID'] == None:

                raise ConfigurationException(
                    "** Application Name (zoneID) property is required")

            elif self._configs['deviceId'] == None:

                raise ConfigurationException(
                    "** Device Name (deviceId) property is required")

            elif self._configs['deviceName'] == None:

                raise ConfigurationException(
                    "** Device Name (deviceName) property is required")

            elif self._configs['username'] == None:

                raise ConfigurationException(
                    "** MQTT UserName (username) property is required")

            elif self._configs['password'] == None:

                raise ConfigurationException(
                    "** MQTT Password (password) property is required")

            print("-- JumpWayMQTT Device Initiated")

        def connectToDevice(self):

            print("-- JumpWayMQTT Device Connection Initiating")

            deviceStatusTopic = '%s/Devices/%s/%s/Status' % (
                self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])

            self.mqttClient = mqtt.Client(
                client_id=self._configs['deviceName'], clean_session=False)
            self.mqttClient.will_set(deviceStatusTopic, "OFFLINE", 0, False)
            self.mqttClient.tls_set(self.mqttTLS, certfile=None, keyfile=None)
            self.mqttClient.on_connect = self.on_connect
            self.mqttClient.on_message = self.on_message
            self.mqttClient.on_publish = self.on_publish
            self.mqttClient.on_subscribe = self.on_subscribe
            self.mqttClient.username_pw_set(
                str(self._configs['username']), str(self._configs['password']))
            self.mqttClient.connect(self.mqttHost, self.mqttPort, 10)
            self.mqttClient.loop_start()

            print("-- JumpWayMQTT Device Connection Initiated")

        def on_connect(self, client, obj, flags, rc):

            print("-- JumpWayMQTT Device Connected")
            print("rc: "+str(rc))

            self.publishToDeviceStatus("ONLINE")

        def on_subscribe(self, client, obj, mid, granted_qos):

            print("JumpWayMQTT Subscription: " +
                  str(self._configs['deviceName']))

        def on_message(self, client, obj, msg):

            print("JumpWayMQTT Message Received")
            splitTopic = msg.topic.split("/")

            if splitTopic[4] == 'Commands':

                if self.deviceCommandsCallback == None:

                    print(
                        "** Device Commands Callback Required (deviceCommandsCallback)")

                else:

                    self.deviceCommandsCallback(msg.topic, msg.payload)

            elif splitTopic[4] == 'Keys':

                if self.deviceKeysCallback == None:

                    print("** Device Keys Callback Required (deviceKeysCallback)")

                else:

                    self.deviceKeysCallback(msg.topic, msg.payload)

            elif splitTopic[4] == 'SSLs':

                if self.deviceSSLsCallback == None:

                    print("** Device SSLs Callback Required (deviceSSLsCallback)")

                else:

                    self.deviceSSLsCallback(msg.topic, msg.payload)

        def subscribeToDeviceChannel(self, channelID, qos=0):

            print("-- Subscribing JumpWayMQTT To Device Topic")

            if self._configs['locationID'] == None:

                print("** Device Location ID Required (locationID)")
                return False

            elif self._configs['zoneID'] == None:

                print("** Device Zone ID Required (zoneID)")
                return False

            elif self._configs['deviceId'] == None:

                print("** Device ID Required (deviceId)")
                return False

            elif channelID == None:

                print("** Device Channel ID Required (channelID)")
                return False

            else:

                deviceChannel = '%s/Devices/%s/%s/%s' % (
                    self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'], channelID)
                self.mqttClient.subscribe(deviceChannel, qos=qos)
                print("-- Subscribed to Device " +
                      self._configs['deviceId']+" Channel "+channelID)
                return True

        def publishToDeviceStatus(self, data):

            if self._configs['locationID'] == None:

                print("** Device Location ID Required (locationID)")
                return False

            elif self._configs['zoneID'] == None:

                print("** Device Zone ID Required (zoneID)")
                return False

            elif self._configs['deviceId'] == None:

                print("** Device ID Required (deviceId)")
                return False

            else:

                deviceStatusTopic = '%s/Devices/%s/%s/Status' % (
                    self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
                self.mqttClient.publish(deviceStatusTopic, data)
                print("-- Published to Device Status ")

        def publishToDeviceChannel(self, channelID, data):

            if self._configs['locationID'] == None:

                print("** Device Location ID Required (locationID)")
                return False

            elif self._configs['zoneID'] == None:

                print("** Device Zone ID Required (zoneID)")
                return False

            elif self._configs['deviceId'] == None:

                print("** Device ID Required (deviceId)")
                return False

            elif channelID == None:

                print("** Device Channel ID Required (channelID)")
                return False

            else:

                deviceChannel = '%s/Devices/%s/%s/%s' % (
                    self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'], channelID)
                self.mqttClient.publish(deviceChannel, json.dumps(data))
                print("-- Published to Device "+channelID+" Channel")

        def on_publish(self, client, obj, mid):

            print("-- Published: "+str(mid))

        def on_log(self, client, obj, level, string):

            print(string)

        def disconnectFromDevice(self):
            self.publishToDeviceStatus("OFFLINE")
            self.mqttClient.disconnect()
            self.mqttClient.loop_stop()
