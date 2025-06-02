import machine
import utime

class Button:
    
    def __init__(self, pin, handler_function=None, debounce_ms=200):
        self.pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.handler_function=handler_function
        self.debounce_ms = debounce_ms
        self.last_press_time = 0
        self.pin.irq(trigger=machine.Pin.IRQ_RISING, handler=self.irq_handler)

    def is_pressed(self):
        return self.pin.value() == 1
    
    def irq_handler(self, pin):
        if self.is_pressed():
            current_time = utime.ticks_ms()
            if utime.ticks_diff(current_time, self.last_press_time) > self.debounce_ms: #se il tempo passato dal preceente click è maggiore del debounce
                self.last_press_time = current_time
                if self.handler_function: #se ho passato la handler_function
                    self.handler_function()
        

    
    

