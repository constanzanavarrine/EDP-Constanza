from ClasePersona import Persona 
# empleado hereda de persona 
class Empleado(Persona):
    
    # constructor
    def __init__(self, nombre, ident, edad, sexo,cargo,salario,legajo): # caracteristicas de la persona + caracteristicas propias 
       
        # super().__init__(nombre, ident, edad, sexo)
        
        Persona.__init__(self,nombre,ident,edad,sexo)
        
        self.cargo = cargo
        self.salario = salario
        self.legajo = legajo 
    
    
    def __str__(self):
        return 'Me llamo {} y mi cargo es {}'.format(self.nombre, self.cargo)
    


daniela = Empleado('Daniela',973922,25,'F','Gerente',500000,1121)
print(daniela)

pedro = Persona('Pedro',5627222,2,'M')
print(pedro)
print(pedro.mayor_edad())