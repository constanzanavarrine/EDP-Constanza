'''
Crea una clase llamada ListaEnlazada que almacena la información de los estudiantes de Estructuras de Datos. 
Todo estudiante es una persona y debe tener como atributos adicionales el listado de las materias que está viendo, 
legajo y carrera que estudia. La lista debe tener como atributo un nodo cabeza. Usted debe implementar los siguientes métodos:

Agregar los estudiantes a la lista organizados por orden alfabético por apellido
Eliminar un estudiante de la lista dado su legajo
Visualizar la materia el promedio de materias que ven los estudiantes
Visualizar la información de cada estudiante incluyendo el listado de las materias que está viendo


'''
import copy
from typing import List
from validador import Validador as V

class Nodo():
    def __init__(self, dato):
        self.dato = dato               # dato guardado en el nodo
        self.siguiente=None
    def __str__(self):
        siguiente= self.siguiente.dato if self.siguiente else None
        return f"{self.dato} y mi siguiente es {siguiente}"



class Persona():
    '''Contruir mis objetos'''    
    def __init__(self, nombre:str, apellido:str, dni:str, edad:int):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.apellido = apellido 
        
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


class Estudiante(Persona):
    def __init__(self, nombre: str, apellido:str, dni: int, edad: int , materias: List, legajo: int, carrera: str):
        super().__init__(nombre, apellido, dni, edad)
        self.materias = materias
        self.legajo = V.validar_entero(legajo, 'Legajo')
        self.carrera = V.validar_cadena_no_vacia(carrera, 'Carrera')
        self.carrera = V.validar_solo_letras(carrera, 'Carrera')
    
    def __repr__(self):
        return (f'Nombre: {self.nombre} | Apellido: {self.apellido} | DNI: {self.dni} | Edad: {self.edad} | '
                f'Legajo: {self.legajo} | Carrera: {self.carrera} | Materias en curso: {self.materias}')
    

class ListaEnlazada():
    '''
    Almacena la informacion de los estudiantes 
    Todo estudiante es una persona y debe tener como atributos adicionales el listado
    de materias que esta viendo, el legajo y carrera que estudia 
    
    Lista -> atributos -> nodo cabeza 
    
    '''
    
    def __init__(self):
        self.inicio = None 
        
    
    def esVacia(self):
        return self.inicio == None
    
    
    def agregar_estudiante(self, estudiante):
        #Agregar los estudiantes a la lista organizados por orden alfabético por apellido
        
        if not isinstance(estudiante, Estudiante):
            raise V.ValidationError('No es posible agregar el dato a la lista. Debe ser un estudiante valido')
        
        nodo_nuevo = Nodo(estudiante)
        if self.esVacia():
            self.inicio = nodo_nuevo
            return
        # Si el nuevo estudiante va antes del primero
        if estudiante.apellido < self.inicio.dato.apellido:
            nodo_nuevo.siguiente = self.inicio
            self.inicio = nodo_nuevo
            return
        
        # Buscar la posición correcta
        actual = self.inicio
        
        while actual.siguiente and estudiante.apellido > actual.siguiente.dato.apellido:
            actual = actual.siguiente
        nodo_nuevo.siguiente = actual.siguiente
        actual.siguiente = nodo_nuevo
        
    def a_lista(self):   # metodo para mostrar en formato lista
        out = []
        actual = self.inicio
        while actual:
            out.append(actual.dato)
            actual = actual.siguiente
        return out
        
        
        # En el ciclo while trabajamos con actual siguiente porque
        # queremos encontrar el lugar donde insertar el nuevo nodo antes de que el APELLIDO
        # DEL SIGUIENTE sea maor o igual al del nuevo estudiante 
        
        
        

    def eliminar_estudiante(self, legajo):
        #Eliminar un estudiante de la lista dado su legajo
        
        if not isinstance(legajo, self.legajo):
            raise V.ValidationError('No se ingreso un dato valido')
        
        if self.esVacia():
            print('No hay estudiantes para eliminar, la lista se encuentra vacia')
        
        else:
            actual = self.inicio
            previo = None
            encontrado = False 
            while True:
                if actual.dato == legajo:
                    encontrado = True
                    break 

                previo = actual # guardo el nodo previo
                actual = actual.siguiente

            if encontrado:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente

            else:
                raise ValueError('El valor no se encuentra en la lista')
        
        
        
        
        
        
        
        
        
    
    # def visualizar_info_estudiante():
    #     pass



    

if __name__ == "__main__":
    
    lista = ListaEnlazada()
    estudiante1 = Estudiante('Constanza', 'Navarrine', 44714389, 22, ['Estructuras de Datos', 'Gestion de datos', 'Analisis II', 'Analisis III'], 62846, 'Ingenieria Industrial')
    estudiante2 = Estudiante('Juana', 'Ercolessi', 46920022, 20, ['Estructuras de Datos', 'Gestion de datos', 'Analisis II', 'Analisis III'], 64846, 'Ingenieria Industrial')
    estudiante3 = Estudiante('Renata', 'Salvarezza', 46921022, 20, ['Estructuras de Datos', 'Gestion de datos', 'Analisis II', 'Analisis III'], 64846, 'Ingenieria Industrial')
    
    lista.agregar_estudiante(estudiante1)
    lista.agregar_estudiante(estudiante2)
    lista.agregar_estudiante(estudiante3)
    print(lista.a_lista())
    
     