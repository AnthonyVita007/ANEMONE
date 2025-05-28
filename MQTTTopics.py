

topic_pub = b"dispenser/avviso"      # topic dove l'ESP pubblica lo stato (presa medicina)
topic_sub = b"dispenser/comando"     # topic da cui l'ESP riceve comandi (es. 'avvia', 'resetta')



# Funzione chiamata quando arriva un messaggio MQTT sul topic_sub
def sub_callback(topic, msg):
    print("📩 Messaggio ricevuto:", topic, msg) 
    if topic == topic_sub:
        # giorno_fascia = topic.split("/")[-1]
        # if giorno_fascia == "lunedi_mattina" and msg == b"avvia":
         #   suona_buzzer() 
        if msg == b"avvia":
            suona_buzzer()
            # funzione per rotazione dello step motor corrispondente al giorno e all'ora ( al topic) del messaggio 
            # funzione per acensione del led sepre in funzione del topic
        elif msg == b"resetta":
            print("↩️ Reset alla posizione di partenza")
            led.off()  # Spegne il LED come esempio di reset


