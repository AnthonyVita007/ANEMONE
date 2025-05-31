import network
from machine import Pin
from time import sleep
import time
import machine

class WiFiConnector:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wifi_interface = network.WLAN(network.STA_IF)

    def connect(self, timeout_s=30):
        print("🔌Connessione alla rete WiFi in corso")

        # spegnimento e riaccensione scheda wifi
        self.wifi_interface.active(False)
        time.sleep(1)
        self.wifi_interface.active(True) # Attiva l'interfaccia Wi-Fi
        self.wifi_interface.connect(self.ssid, self.password)
        
        #tentativo di connessione gestito con timeout di 30s
        start_time = time.time() # Registra il tempo di inizio per il timeout
        while not self.wifi_interface.isconnected():
            if time.time() - start_time > timeout_s:
                raise Exception("Timeout di connessione Wi-Fi scaduto")
        
        #se supera il while allora si è connesso
        print("\nConnesso!")
        print("Info rete:", self.wifi_interface.ifconfig())
        return self.wifi_interface
