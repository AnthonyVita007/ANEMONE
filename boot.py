import network
from machine import Pin
from time import sleep
import time
import machine
import boot
import MQTTTopics
import stepMotor
import connectionBrokerMQTT
from Buzzer import *
from umqtt.simple import MQTTClient

class WiFiConnector:
    def __init__(self, ssid='', password=''):
        self.ssid = ssid
        self.password = password
        self.sta_if = network.WLAN(network.STA_IF)

    def connect(self):
        print("🔌 Connessione alla rete WiFi in corso...", end="")
        self.sta_if.active(True)
        self.sta_if.connect(self.ssid, self.password)

        while not self.sta_if.isconnected():
            pass  # attende finché non è connesso

        print(" ✅ Connesso!")
        print("📶 Info rete:", self.sta_if.ifconfig())
        return self.sta_if

