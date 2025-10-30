# materia
# nivel educativo
# laboratorio (si/no)
# en este tipo de herencia libroacademico puede acceder al padre libro pero
# libro (padre) no puede acceder a libro academico 


from libro import Libro 

# libro academico hereda de libro todos los atributos y metodos pero
# agrego materia, nivel educativo y laboratorio 

class LibroAcademico(Libro):
    
    # constructor
    
    niveles_validos = ['primaria', 'secundaria', 'universidad', 'posgrado']
    
    # variables definidas (como requiere lab) -> van al final
    def __init__(self, titulo, autor, editorial, ISBN: str, materia: str, nivel: str, estado='disponible', requiere_laboratorio = False):
        
        # super es el "padre"
        # siempre los parametros deben ir en el mismo orden 
        # los parentesis son de quien heredo 
        # con super no va el self
        super().__init__(titulo, autor, editorial, ISBN, estado)
        
            # otra forma de super 
            # en esta forma debe ir si o si SELF
                #Libro.__init__(self,titulo, autor, editorial, ISBN, estado)
        
        
        self.materia = self.validar_cadena(materia)          # cadena y que no este vacia 
        self.nivel = nivel 
        self.requiere_laboratorio = requiere_laboratorio
    
    
    def setter_estado(self,nivel):
        nivel = nivel.lower()
        if estado not in LibroAcademico.niveles_validos:
            raise ValueError(f'El nivel debe ser uno de los siguientes: {self.niveles_validos}')
    
    
    def requieres_laboratorio(self, requiere_laboratorio: bool):
        if not isinstance(requiere_laboratorio, bool):
            raise TypeError('El tipo de dato debe ser un bool')
        return requiere_laboratorio
    
    
    def __str__(self):
        frase_saludo = super().__str__()
        if self.requiere_laboratorio == True:
            laboratorio = 'Requiere laboratorio'
        
        else:
            laboratorio = 'No requiere laboratorio'
        
        return f'{frase_saludo}. Es un libro de {self.materia} del nivel {self.nivel} y {laboratorio}'
        
  
  
  
if __name__ == '__main__': # si cuando no soy yo -> no se ejecuta
    try:  
        fisica = LibroAcademico('Fisica I', 'No me molestes', 'Sufrir', '1234', 'Fisica', 'Universitario', requiere_laboratorio=True )
        print(fisica)
        print(LibroAcademico.__mro__)  # -> muestra como python comienza la busqueda de metodos y en que orden cuando trabaja con herencia
                                       # -> es util para el parcial  
    
    except TypeError as e:
        print('El error es:',e)
    except ValueError as e:
        print('El error es:',e)
    except Exception as e:
        print('El error es:',e) 