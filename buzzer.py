from machine import Pin, PWM
from time import sleep_ms

class Buzzer:
    def __init__(self, sig_pin, duty):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))
        self.pwm.duty(0) #il buzzer parte "muto"
        self.duty=duty
        
    def play(self, melody, wait):
        for note in melody:
            if note == P: 
                self.pwm.duty(0) #pausa
            else:
                self.pwm.freq(note)
                self.pwm.duty(self.duty)
            sleep_ms(wait) #piccola pausa per separare le note
        self.stop()

    def stop(self):
        self.pwm.duty(0)

LA3 = 220
DO = 262
RE = 294
MI = 330
FA = 349
SOL = 392
LAb = 415
LA = 440
SIb = 466
SI = 494
DO5 = 523
DOd5 = 554
RE5 = 587
MIb5 = 627
MI5 = 659
P = 0 #pausa


MELODY = [MI,FA,SOL,P,FA,P,MI,RE,P,P,DO,P,RE,MI,P,P,P,P,P,
        MI,FA,SOL,P,FA,P,MI,RE,P,P,DO,P,RE,MI,P,P,P,P,P,
        MI,FA,SOL,P,FA,P,MI,RE,P,P,DO,P,RE,MI,P,P,P,P,P,
          MI,FA,SOL,P,FA,P,MI,RE,P,P,SOL,P,LA,P,SOL,FA,P,MI,RE,P,DO,LA3
          ]

MELODY2 = [P,SOL,LA,SI,DOd5,SOL,LA,SI,DOd5,
         LAb,SIb,DO5,RE5,LAb,SIb,DO5,RE5,
         LA,SI,DOd5,MIb5,LA,SI,DOd5,MIb5,P,
         LA,SIb,SI,DO5,DO5,P]