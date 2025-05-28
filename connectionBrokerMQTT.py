import ubinascii
import MQTTTopics
from machine import Pin
from time import sleep
import network
import time
import machine
import boot
import stepMotor
import connectionBrokerMQTT
from Buzzer import *
from umqtt.simple import MQTTClient

import ubinascii
import machine
import time
from umqtt.simple import MQTTClient

class Connector:
    def __init__(self, mqtt_server, topic_sub, sub_callback, mqtt_user="", mqtt_password=""):
        self.mqtt_server = mqtt_server
        self.topic_sub = topic_sub
        self.sub_callback = sub_callback
        self.mqtt_user = mqtt_user
        self.mqtt_password = mqtt_password
        self.client_id = ubinascii.hexlify(machine.unique_id())
        self.client = None

    def connect_and_subscribe(self):
        try:
            self.client = MQTTClient(self.client_id, self.mqtt_server, user=self.mqtt_user, password=self.mqtt_password)
            self.client.set_callback(self.sub_callback)
            self.client.connect()
            self.client.subscribe(self.topic_sub)
            print("📡 Connesso al broker MQTT e sottoscritto al topic:", self.topic_sub)
            return self.client
        except OSError:
            self.restart_and_reconnect()

    def restart_and_reconnect(self):
        print('⚠️ Errore MQTT. Riavvio...')
        time.sleep(10)
        machine.reset()
