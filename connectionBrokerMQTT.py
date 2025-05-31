import ubinascii
from machine import Pin
from time import sleep
import network
import time
import machine
import boot
import stepMotor
import connectionBrokerMQTT
from buzzer import *
from umqtt.simple import MQTTClient

import ubinascii
import machine
import time
from umqtt.simple import MQTTClient

import ubinascii
import machine
import time
from umqtt.simple import MQTTClient

class MQTT_manager:
    #COSTRUTTORE
    def __init__(self, mqtt_server, mqtt_user="", mqtt_password=""):
        self.mqtt_server = mqtt_server
        self.mqtt_user = mqtt_user
        self.mqtt_password = mqtt_password
        self.client_id = ubinascii.hexlify(machine.unique_id())
        self.client = None
        self.callback_function = None

    #metodo per connettersi al broker MQTT
    def connect_to_MQTT_broker(self):
        try:
            self.client = MQTTClient(
                self.client_id, 
                self.mqtt_server, 
                user=self.mqtt_user, 
                password=self.mqtt_password
            )
            if self.callback_function:
                self.client.set_callback(self.callback_function)
            self.client.connect()
            print("📡 Connesso al broker MQTT.")
        except OSError as e:
            print("❌ Errore durante la connessione al broker MQTT:", e)
            self.restart_and_reconnect()

    #metodo per sottoscrivere la esp32 ad un topic
    def subscribe_to_topic(self, topic_name):
        if self.client:
            self.client.subscribe(topic_name)
            print("✅ Sottoscritto al topic:", topic_name)
        else:
            print("⚠️ Client MQTT non connesso. Impossibile sottoscrivere al topic.")

    #metodo per settare la funzione di callback che gestisce i messaggi in arrivo dai topic sottoscritti
    def set_callback(self, callback_function):
        self.callback_function = callback_function
        if self.client:
            self.client.set_callback(callback_function)
        print("📲 Callback impostata.")

    # metodo per pubblicare un messaggio su un topic specifico
    def publish_on_topic(self, topic_name, message):
        if self.client:
            try:
                self.client.publish(topic_name, message)
                print(f"📤 Messaggio pubblicato su '{topic_name}': {message}")
            except Exception as e:
                print("❌ Errore durante la pubblicazione:", e)
        else:
            print("⚠️ Client MQTT non connesso. Impossibile pubblicare il messaggio.")

    # metodo per controllare l'arrivo di nuovi messaggi MQTT e richiamare la callback
    def check_messages_from_topics(self):
        if self.client:
            try:
                self.client.check_msg()
            except Exception as e:
                print("❌ Errore durante il controllo dei messaggi MQTT:", e)
        else:
            print("⚠️ Client MQTT non connesso. Impossibile controllare i messaggi.")

        
    #metodo di reset in caso di errore di connessione
    def restart_and_reconnect(self):
        print('🔄 Riavvio in corso tra 10 secondi...')
        time.sleep(10)
        machine.reset()

