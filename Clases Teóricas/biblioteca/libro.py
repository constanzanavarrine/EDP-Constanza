class Libro:
    # constructor
    posibles_estados = ['disponible','prestado']     # atributo de clase
    contador_libros = 0                              # atributo de clase (por fuera del init)
    
    
    
    # self -> sobre un determinado objeto 
    #      -> propio de cada objeto 
    # el estado por defecto es disponible (es lo que queremos cada vez que cramos un nuevo libro)
    
    def __init__(self,titulo:str,autor:str,editorial:str,ISBN:str,estado='disponible'): # aca lo que hago es construir el objeto 
        
        self.titulo=self.validar_cadena(titulo) # atributos de instancia → (es igual a lo que llega por parametro)
        self.autor=self.validar_cadena(autor)
        self.editorial=self.validar_cadena(editorial)
        self.ISBN=ISBN                          # (identificador unico)
        self.estado=self.setter_estado(estado)
        Libro.contador_libros += 1          # Libro.() porque siempre debe hacer referencia a la clase que pertenece
   
    
    #visualizar la información de cada libro
    # es un metodo por defecto de Python para la visualizacion 
    # de instancia porque tiene self
    
    def __str__(self):
        # devuelve siempre una cadena
        return f' El libro {self.titulo} es del autor {self.autor} y la editorial es {self.editorial } con ISBN{self.ISBN}, y su estado es {self.estado}'
    
    
    def mostrar(self):
        return f' El libro {self.titulo} es del autor {self.autor} y la editorial es {self.editorial } con ISBN{self.ISBN}, y su estado es {self.estado}'


    def getter_estado(self):
        return self.estado
    
    
    def getter_ISBN(self):# no se ha validado, puede construir un objeto libro incorrecto al pasar un ISBN no valido
        return self.ISBN
    


    def devolver_libro(self):
        if self.estado=='disponible':
            print('El libro ya se encuentra disponible')
        else:
            self.setter_estado('disponible')
            print('El libro ha sido devuelto y se encuentra disponible')
    
    
    def prestar_libro(self):
        if self.getter_estado()=='disponible':
            self.estado='prestado'
            print(f'El libro {self.titulo} fue prestado con exito')
        else:
            print(f' El libro {self.titulo} no se encuentra disponible para prestar')
    
    
    def validar_cadena(self,cadena:str):
        if not isinstance(cadena,str):
            raise TypeError('El titulo debe ser una cadena de texto')
        if len(cadena)==0:
            raise ValueError('El titulo no puede estar vacio')
        return cadena
 
 
 
    def setter_estado(self,estado):
        estado=estado.lower()
        if estado not in Libro.posibles_estados:
            raise ValueError(f'El estado debe ser uno de los siguientes: {self.posibles_estados}')
        self.estado=estado
        return estado
    
    
    
    def __eq__(self, otro):
        # metodo que permite verificar que dos objetos sean iguales 
        
        # necesitamos verificar primero que otro sea un libro 
        if not isinstance(otro, Libro):
            # isinstance sirve para verificar el tipo de variable u objeto
            raise TypeError('El objeto debe ser una istancia de la clase Libro')
        
        elif id(self) == id(otro):
            return True
        
        elif self.ISBN == otro.ISBN:
            return True
        
        else:
            return False
        
    
    
    @classmethod #(decorador siempre debe ir cuando trabajamos con metodos de clases)
                 # siempre va antes de cada clase  
                 
    # cuantos libros se crearon en un momento determinado? 
        # como lo representamos como un metodo de clase?
    def mostrar_contador_libros(cls):     # cls -> palabra para identificar la clase donde estoy parado
        
        print(f'El numero de libros creados es: {cls.contador_libros}')
    
    
    
    

               
# prueba de la clase
# para probar la clase si o si hacemos los try except 
if __name__ == '__main__': # si cuando no soy yo -> no se ejecuta
    try:
        carlos=Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567890')
        print(carlos)
        print(carlos.mostrar())
        carlos.setter_estado('prestado')
        print(carlos.getter_estado())
        
        carlos1 = Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567891')
        carlos2 = Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567890')
        print(carlos == carlos2)
        print(carlos == carlos1)
        
    except TypeError as e:
        print('El error es:',e)
    except ValueError as e:
        print('El error es:',e)
    except Exception as e:
        print('El error es:',e)
    
    
    
    
    
    