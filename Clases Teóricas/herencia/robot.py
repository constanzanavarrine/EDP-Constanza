class Robot:
    def __init__(self,nombreRobot:str,modelo:str,dniRobot:str):
        self.nombreRobot=nombreRobot
        self.modelo=modelo
        self.dniRobot=dniRobot
        
    def __str__(self):
        return f"Nombre del robot: {self.nombreRobot} y el modelo es  {self.modelo} y identificador {self.dniRobot}"
    
    def getNombre(self):
        return self.nombreRobot
    
    def setnombreRobot(self,nombre):
        self.nombreRobot=nombre
        

if __name__=='__main__':
    robot1=Robot("R2D2","Asistente","123456")
    print(robot1)
        