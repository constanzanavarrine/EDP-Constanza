from libroAcademico import LibroAcademico
from libro import Libro

#construir libro Academico Universitario

class Libro_Academico_Universitario(LibroAcademico):
    
    def __init__(self, titulo, autor, editorial, ISBN, materia, nivel,carrera:str, estado='disponible', requiere_laboratorio=False):
        super().__init__(titulo, autor, editorial, ISBN, materia, nivel, estado, requiere_laboratorio)
        self.carrera=carrera
    
    def __str__(self):
        return f'{self.titulo}'

if __name__=='__main__':
    carlos=Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567890')
    estructuras=Libro_Academico_Universitario('fisica 1','No me molestes','sufrir','12345','Fisica','universitario','Ingenieria Industrial',requiere_laboratorio=True)
    print(estructuras)
    print(estructuras.contador_libros)
    