class Persona():
    # creacion del constructor 
    def __init__(self,nombre,ident,edad,sexo):
        # agregamos informacion al objeto que llega 
        self.nombre = nombre
        self.ident = ident
        self.edad = edad
        self.sexo = sexo
    
    # visualizo la informacion del objeto 
    # metodo visualizacion
    def __str__(self):
        cadena = ''
        cadena = 'La persona llamada {} tiene DNI {}, su edad es {}'.format(self.nombre,self.ident,self.edad)
        return cadena 
    
    # metodo mayor de edad
    def mayor_edad(self):
        return self.edad >= 21
    
    # para diccionarios 
    def __repr__(self):
        return self.__str__()



# si yo me llamo a mi misma, imprimo

if __name__ == '__main__':
    
    # cramos los objetos por fuera de la clase 
    daniela = Persona('Daniela',973922,25,'F')
    
    print(daniela)
    
    daniela.edad = 30  # actualizo la edad de daniela 
    
    print(daniela)
    
    print(daniela.mayor_edad())