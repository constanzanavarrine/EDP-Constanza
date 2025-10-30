from persona import *
from robot import Robot

class Humanoides(Persona,Robot):
    def __init__(self, nombre:str,dni:str,edad:str,nombreRobot:str,modelo:str,dniRobot:str):
        Persona.__init__(self,nombre,dni,edad)
        Robot.__init__(self,nombreRobot,modelo,dniRobot)       
    
    def __str__(self):
        return f"Hola soy {self.nombre} y soy un robot {self.nombreRobot} modelo {self.modelo}"
    

humanoide1=Humanoides('NinfaRobot','123345',50,'Ninfa Robot','ahqet','robot1234')
print(humanoide1)
print(humanoide1.getNombre())
print(Humanoides.__mro__)