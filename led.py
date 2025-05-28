from machine import Pin

class LED:
        def __init__(self, pin):
            self.pin = Pin(pin, Pin.OUT)
            
        def switch(self):
            self.pin.value(not self.pin.value())

        def on(self):
             self.pin.on()
            
        def off(self):
             self.pin.off()