from machine import Pin

class Infrared:

    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN)

    def value(self):
        return self.pin.value()