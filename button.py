import machine
import utime

class Button:
    
    def __init__(self, pin, debounce_ms=200):
        self.pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.debounce_ms = debounce_ms
        self.last_press_time = 0
        
    def is_pressed(self):
        return self.pin.value() == 0
    
    def set_irq(self,step,client,topic):
        self.pin.irq(handler=self.was_clicked(step,client,topic), trigger=self.pin.IRQ_FALLING)
    
    def was_clicked(self, step, client, topic_pub):
        if self.is_pressed():
            current_time = utime.ticks_ms()
            if utime.ticks_diff(current_time, self.last_press_time) > self.debounce_time: #se il tempo passato dal preceente click è maggiore del debounce
                self.last_press_time = current_time
                step.return_to_home()
                client.publish(topic_pub,"Ritorno in posizione di start")
                return True
        return False
        

    
    

