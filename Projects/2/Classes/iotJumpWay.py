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
# Last Modified: 2020-06-19
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

        print("-- Initiating JumpWayMQTT Device")

        self.Helpers = Helpers("iotJumpWay")
        self.confs = configs

        self.mqttClient = None
        self.mqttTLS = "/etc/ssl/certs/DST_Root_CA_X3.pem"
        self.mqttHost = self.confs['host']
        self.mqttPort = self.confs['port']

        self.deviceStatusCallback = None
        self.deviceCommandsCallback = None
        self.deviceSensorCallback = None
        self.deviceTriggerCallback = None

        if self.confs['lid'] == None:
            raise ConfigurationException(
                "** Location ID (lid) property is required")
        elif self.confs['zid'] == None:
            raise ConfigurationException(
                "** Application Name (zid) property is required")
        elif self.confs['did'] == None:
            raise ConfigurationException(
                "** Device Name (did) property is required")
        elif self.confs['dn'] == None:
            raise ConfigurationException(
                "** Device Name (deviceName) property is required")
        elif self.confs['un'] == None:
            raise ConfigurationException(
                "** MQTT UserName (username) property is required")
        elif self.confs['pw'] == None:
            raise ConfigurationException(
                "** MQTT Password (password) property is required")

        self.Helpers.logger.info("JumpWayMQTT Device Initiated.")
        
    def connect(self):

        self.Helpers.logger.info("JumpWayMQTT Device Connection Initiating")

        deviceStatusTopic = '%s/Devices/%s/%s/Status' % (
            self.confs['lid'], self.confs['zid'], self.confs['did'])

        self.mqttClient = mqtt.Client(
            client_id=self.confs['dn'], clean_session=False)
        self.mqttClient.will_set(deviceStatusTopic, "OFFLINE", 0, False)
        self.mqttClient.tls_set(self.mqttTLS, certfile=None, keyfile=None)
        self.mqttClient.on_connect = self.on_connect
        self.mqttClient.on_message = self.on_message
        self.mqttClient.on_publish = self.on_publish
        self.mqttClient.on_subscribe = self.on_subscribe
        self.mqttClient.username_pw_set(
            str(self.confs['un']), str(self.confs['pw']))
        self.mqttClient.connect(self.mqttHost, self.mqttPort, 10)
        self.mqttClient.loop_start()

        self.Helpers.logger.info("JumpWayMQTT Device Connection Initiated")

    def on_connect(self, client, obj, flags, rc):
    
        self.Helpers.logger.info("JumpWayMQTT Device Connected")
        self.Helpers.logger.info("JumpWayMQTT Connection rc: "+str(rc))

        self.deviceStatusPub("ONLINE")

    def on_subscribe(self, client, obj, mid, granted_qos):

        self.Helpers.logger.info("JumpWayMQTT Subscription: " + str(self.confs['deviceName']))

    def on_message(self, client, obj, msg):

        self.Helpers.logger.info("JumpWayMQTT Message Received")
        splitTopic = msg.topic.split("/")

        if splitTopic[4] == 'Commands':
            if self.deviceCommandsCallback == None:
                self.Helpers.logger.info("Device Commands Callback Required (deviceCommandsCallback)")
            else:
                self.deviceCommandsCallback(msg.topic, msg.payload)
        elif splitTopic[4] == 'Status':
            if self.deviceStatusCallback == None:
                self.Helpers.logger.info("Device Keys Callback Required (deviceStatusCallback)")
            else:
                self.deviceStatusCallback(msg.topic, msg.payload)
        elif splitTopic[4] == 'Sensors':
            if self.deviceSensorsCallback == None:
                self.Helpers.logger.info("Device Keys Callback Required (deviceSensorsCallback)")
            else:
                self.deviceSensorsCallback(msg.topic, msg.payload)
        elif splitTopic[4] == 'Trigger':
            if self.deviceSensorsCallback == None:
                self.Helpers.logger.info("Device Keys Callback Required (deviceTriggerCallback)")
            else:
                self.deviceTriggerCallback(msg.topic, msg.payload)

    def subscribe(self, channelID, qos=0):

        self.Helpers.logger.info("Subscribing JumpWayMQTT To Device Topic: " + channelID)
        
        if channelID == None:
            self.Helpers.logger.info("Device Channel ID Required (channelID)")
            return False
        else:
            deviceChannel = '%s/Devices/%s/%s/%s' % (
                self.confs['lid'], self.confs['zid'], self.confs['did'], channelID)
            self.mqttClient.subscribe(deviceChannel, qos=qos)
            self.Helpers.logger.info("Subscribed to Device " + self.confs['did']+" Channel "+channelID)
            return True

    def deviceStatusPub(self, data):

        deviceStatusTopic = '%s/Devices/%s/%s/Status' % (
            self.confs['lid'], self.confs['zid'], self.confs['did'])
        self.mqttClient.publish(deviceStatusTopic, data)
        self.Helpers.logger.info("Published to Device Status")

    def devicePub(self, channelID, data):
        
        if channelID == None:
            self.Helpers.logger.info("Device Channel ID Required (channelID)")
            return False
        else:
            deviceChannel = '%s/Devices/%s/%s/%s' % (
                self.confs['lid'], self.confs['zid'], self.confs['did'], channelID)
            self.mqttClient.publish(deviceChannel, json.dumps(data))
            self.Helpers.logger.info("Published to Device "+channelID+" Channel")

    def on_publish(self, client, obj, mid):

        print("-- Published: "+str(mid))

    def on_log(self, client, obj, level, string):

        print(string)

    def disconnect(self):
        self.deviceStatusPub("OFFLINE")
        self.mqttClient.disconnect()
        self.mqttClient.loop_stop()
