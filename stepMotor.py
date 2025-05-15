from machine import Pin
from time import sleep

class StepMotor:
    
    #ATTRIBUTI
    #costante che definisce quante sequenze da 4 step sono necessarie per ruotare di un grado il motore
    #dato che una sequenza ha 4 passi, dividiamo per 4
    SEQUENCE_FOR_DEGREE = 2048/(360*4)

    #COSTRUTTORE
    def __init__(self, I1, I2, I3, I4):
        # Attributi di istanza
        self.pins = [
            Pin(I1, Pin.OUT),
            Pin(I2, Pin.OUT),
            Pin(I3, Pin.OUT),
            Pin(I4, Pin.OUT)
        ]
    
    # Sequenza per rotazione antioraria (puoi invertire se serve orario)
        self.sequence_anticlockwise = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        
    # Attributo: sequenze per rotazioni orarie e antiorarie
        self.sequence_clockwise = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

#METODI
#questo metodo fa fare al motore uno step in senso antiorario ovvero 0.176°
    def rotate_anticlockwise(self, degree): 
#Calcolo quanti step sono necessari per ruotare di n gradi
        step_needed = degree*self.SEQUENCE_FOR_DEGREE
        for i in range(int(step_needed)):
                       
#Esecuzione di un passo (0.176° di rotazione)
            for step in self.sequence_anticlockwise:
                for j in range(len(self.pins)):
                    self.pins[j].value(step[j])
#serve per regolare la velocità di rotazione
                    sleep(0.001)

    def rotate_clockwise(self, degree): 
#Calcolo quanti step sono necessari per ruotare di n gradi
        step_needed = degree*self.SEQUENCE_FOR_DEGREE
        for i in range(int(step_needed)):
                       
#Esecuzione di un passo (0.176° di rotazione)
            for step in self.sequence_clockwise:
                for j in range(len(self.pins)):
                    self.pins[j].value(step[j])
#serve per regolare la velocità di rotazione
                    sleep(0.001)
                    
    def rotate_by_day(self, day):
        day_map = {
            "MON": 1,
            "TUE": 2,
            "WED": 3,
            "THU": 4,
            "FRI": 5,
            "SAT": 6,
            "SUN": 7
        }
        
        # Ottieni il numero corrispondente al giorno
        d = day_map.get(day.upper(), None)
        
        if d is not None:
            self.rotate_clockwise(d*45)
        else:
            print("Errore: giorno non valido. Usa MON, TUE, ..., SUN")
