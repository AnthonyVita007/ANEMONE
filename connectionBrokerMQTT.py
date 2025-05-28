# Parametri MQTT
mqtt_server = "broker.hivemq.com"
mqtt_user = ""
mqtt_password = ""
client_id = ubinascii.hexlify(machine.unique_id())

# Connessione al broker MQTT
def connect_and_subscribe():
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_callback)
    client.connect()
    client.subscribe(MQTTTopics.topic_sub)
    print("📡 Connesso al broker MQTT e sottoscritto al topic")
    return client

# Se fallisce la connessione, riavvia
def restart_and_reconnect():
    print('⚠️ Errore MQTT. Riavvio...')
    time.sleep(10)
    machine.reset()