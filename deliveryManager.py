import time
from time import sleep


class DeliveryManager : 
    @staticmethod
    def deliveryFunction (ir,mqtt_manager,step_motor,display,anemone,topic_pub,pillTimeout) :
        print("Entrata in delivery")
        start_time = time.time() # Registra il tempo di inizio per il timeout
        flag_presa = False
        while (time.time() - start_time < pillTimeout) and (not flag_presa):
            if ir.value() == 0:  # Assumendo che '0' significhi che la pillola è stata rilevata
                flag_presa = True
                sleep(0.5)
        if flag_presa :
            mqtt_manager.publish_on_topic(topic_pub,"L'utente ha correttamente prelevato la pillola") # messaggio da cabmiare, inviato all'user su interfaccia
            print("Pillola correttamente prelvata")
            sleep(2)
            display.show_text("Pillola prelevata") # da aggiustare frase
            sleep(30)
            # mqtt_manager.publish_on_topic(topic_pub,"Ritorno in posizione di start")
            display.show_text("Ritorno in posizione di start") # da aggiustare frase
            step_motor.return_to_home()
            print("Ritornato in posizione di start")
            sleep(3)
            display.show_image(anemone)
            return
        else :
            mqtt_manager.publish_on_topic(topic_pub,"L'utente non ha preso la medicina come programmato")
            step_motor.return_to_home()
            display.show_image(anemone)
            return

