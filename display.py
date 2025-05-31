from machine import Pin, I2C
import framebuf
import utime
from ssd1306 import SSD1306_I2C

class Display:
    def __init__(self, scl_pin, sda_pin, width=128, height=64, i2c_id=0):
        self.i2c = I2C(i2c_id, scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.display = SSD1306_I2C(width, height, self.i2c)
        self.width = width
        self.height = height
        self.scl_pin = scl_pin
        self.sda_pin = sda_pin
        self.clear()

    def clear(self):
        """Pulisce lo schermo"""
        self.display.fill(0)
        self.display.show()

    def show_image(self, byte_array, x=0, y=0):
        fb = framebuf.FrameBuffer(byte_array, self.width, self.height, framebuf.MONO_HLSB)
        self.clear()
        for j in range(self.height):
            for i in range(self.width):
                pixel = fb.pixel(i, j)
                self.display.pixel(x + i, y + j, pixel)
        self.display.show()


    def show_text(self, text, x=0, y=0):
        """Mostra del testo sul display"""
        self.clear()
        self.display.text(text, x, y)
        self.display.show()

    def sleep(self, seconds):
        utime.sleep(seconds)


