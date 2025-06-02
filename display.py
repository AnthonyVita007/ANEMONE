from machine import Pin, I2C
import framebuf
import utime
from ssd1306 import SSD1306_I2C

class Display:
    # Costanti per la dimensione del font predefinito
    FONT_WIDTH = 8
    FONT_HEIGHT = 8
    
    def __init__(self, scl_pin, sda_pin, width=128, height=64, i2c_id=0):
        # Inizializza l'interfaccia I2C con i pin specificati
        self.i2c = I2C(i2c_id, scl=Pin(scl_pin), sda=Pin(sda_pin))
        # Inizializza il display SSD1306
        self.display = SSD1306_I2C(width, height, self.i2c)
        self.width = width
        self.height = height
        self.scl_pin = scl_pin
        self.sda_pin = sda_pin
        # Pulisce il display all'avvio
        self.clear()

    def clear(self):
        """Pulisce lo schermo riempiendolo di nero e aggiornando il display."""
        self.display.fill(0)  # Riempi il buffer con 0 (nero)
        self.display.show()   # Aggiorna il display

    def show_image(self, byte_array, x=0, y=0):
        """
        Mostra un'immagine sul display da un array di byte.
        L'immagine viene creata come un FrameBuffer e poi i pixel vengono copiati
        sul display.
        """
        # Crea un FrameBuffer dall'array di byte
        fb = framebuf.FrameBuffer(byte_array, self.width, self.height, framebuf.MONO_HLSB)
        self.clear() # Pulisce lo schermo prima di disegnare l'immagine
        # Copia i pixel dal FrameBuffer dell'immagine al display
        for j in range(self.height):
            for i in range(self.width):
                pixel = fb.pixel(i, j)
                self.display.pixel(x + i, y + j, pixel)
        self.display.show() # Aggiorna il display con l'immagine

    def show_text(self, text, start_x=0, start_y=0):
        """
        Mostra del testo sul display, gestendo automaticamente il "word wrap"
        se il testo supera la larghezza dello schermo.
        """
        
        self.clear() # Pulisce lo schermo prima di disegnare il nuovo testo

        # Calcola il numero massimo di caratteri che possono stare su una riga
        max_chars_per_line = self.width // self.FONT_WIDTH
        
        # Calcola il numero massimo di righe disponibili sul display
        max_lines = self.height // self.FONT_HEIGHT

        current_y = start_y
        words = text.split(' ') # Dividi il testo in parole

        current_line = ""
        line_count = 0

        for word in words:
            # Se l'aggiunta della parola corrente supera la larghezza massima della riga
            # oppure se la riga corrente è vuota e la parola è troppo lunga per una singola riga
            if len(current_line) + len(word) + (1 if current_line else 0) > max_chars_per_line:
                # Se la riga corrente non è vuota, disegnala
                if current_line:
                    if line_count < max_lines:
                        self.display.text(current_line, start_x, current_y)
                        current_y += self.FONT_HEIGHT
                        line_count += 1
                    else:
                        # Troppe righe per il display, interrompi
                        break
                
                # Inizia una nuova riga con la parola corrente
                current_line = word
            else:
                # Aggiungi la parola alla riga corrente
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
        
        # Disegna l'ultima riga rimasta (se non è vuota)
        if current_line and line_count < max_lines:
            self.display.text(current_line, start_x, current_y)

        self.display.show() # Aggiorna il display con tutto il testo

    def sleep(self, seconds):
        """Mette in pausa l'esecuzione per un numero specificato di secondi."""
        utime.sleep(seconds)


