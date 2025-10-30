import copy
class Persona():
    '''Contruir mis objetos'''    
    def __init__(self,nombre:str,dni:str,edad:int):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
    def __str__(self):
        return f'Me llaman {self.nombre} y tengo {self.edad} annos'
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def __eq__(self, otrayo):
        if(id(self)==id(otrayo)):
            return True
        elif self.dni==otrayo.dni and self.nombre==otrayo.nombre:
            return True
        else:
            return False

if __name__=='__main__':
    persona1=Persona('Daniela','12345678',30)
    persona2=Persona('Daniela','12345678',30)
    persona3=copy.copy(persona1)
    persona4=persona1
    print(persona1)
    print(persona1.getNombre())
    persona1.setNombre('Esperanza')
    print(persona1)
    print(persona1==persona2)
    print(persona1==persona3)
    print(Persona.__mro__)  
    del(persona4)# Elimina la referencia 
    print(persona1)