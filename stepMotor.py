from machine import Pin
from time import sleep

class StepMotor:
    
    #ATTRIBUTI
    #costante che definisce quante sequenze da 4 step sono necessarie per ruotare di un grado il motore
    #dato che una sequenza ha 4 passi, dividiamo per 4
    SEQUENCE_FOR_DEGREE = 2048/(360*4)

    #Dato che ho 8 scompartimenti (1 per giorno + 1 standard), ogni 45 gradi cambio giorno
    DEGREES_PER_DAY = 45.3*3

    # Offset iniziale per partire più avanti rispetto alla posizione standard
    INITIAL_OFFSET_DEGREES = 15*3

    DEGREES_PER_ZONE = 15*3
    #COSTRUTTORE
    def __init__(self, I1, I2, I3, I4):
        # Attributi di istanza
        self.pins = [
            Pin(I1, Pin.OUT),
            Pin(I2, Pin.OUT),
            Pin(I3, Pin.OUT),
            Pin(I4, Pin.OUT)
        ]
        self.last_rotation_degree = 0  # salva ultimi gradi ruotati

    
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
                    
    def rotate_by_day(self, day, moment):
        day_map = {
            "MON": 0,
            "TUE": 1,
            "WED": 2,
            "THU": 3,
            "FRI": 4,
            "SAT": 5,
            "SUN": 6
        }

        moment_map = {
            "MORNING":1,
            "AFTERNOON":2,
            "EVENING":3
        }
        
        # Ottiene i numeri corrispondenti al giorno e al momento
        d = day_map.get(day.upper(), None)
        m = moment_map.get(moment.upper(), None)

        if d is not None:
            degree = self.INITIAL_OFFSET_DEGREES + (d * self.DEGREES_PER_DAY + m * self.DEGREES_PER_ZONE) 
            self.last_rotation_degree = degree
            self.rotate_clockwise(degree)
        else:
            print("Errore: giorno o momento non valido. Usa MON, TUE, ..., SUN")

    def return_to_home(self):
        self.rotate_anticlockwise(self.last_rotation_degree)
        self.last_rotation_degree = 0
