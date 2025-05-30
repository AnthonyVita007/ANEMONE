import network
from machine import Pin
from time import sleep
import time
import machine
import boot
import MQTTTopics
import stepMotor
import connectionBrokerMQTT
from umqtt.simple import MQTTClient

class WiFiConnector:
    def __init__(self, ssid='', password=''):
        self.ssid = ssid
        self.password = password
        self.wifi_interface = network.WLAN(network.STA_IF)

    def connect(self):
        print("🔌 Connessione alla rete WiFi in corso...", end="")
        self.wifi_interface.active(True)
        self.wifi_interface.connect(self.ssid, self.password)

        while not self.wifi_interface.isconnected():
            pass  # attende finché non è connesso

        print(" ✅ Connesso!")
        print("📶 Info rete:", self.wifi_interface.ifconfig())
        return self.wifi_interface

