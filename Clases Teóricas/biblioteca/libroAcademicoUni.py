from libroAcademico import LibroAcademico
from libro import Libro

# A esto lo llamamos herencia multinivel (porque libro academico habia heredado de libro)

# construir libro academico universitario 

class Libro_Academico_Universitario(LibroAcademico):
    
    # constructor
    
    def __init__(self, titulo, autor, editorial, ISBN, materia, nivel, carrera: str, estado='disponible', requiere_laboratorio=False):
        super().__init__(titulo, autor, editorial, ISBN, materia, nivel, estado, requiere_laboratorio)
        
        self.carrera = carrera
    
    def __str__(self):
        return f'{self.titulo}'

if __name__ == '__main__':
    estructuras = Libro_Academico_Universitario('Fisica I', 'No me molestes', 'Sufrir', '1234', 'Fisica', 'Universitario', 'Ingenieria Industrial', requiere_laboratorio=True)
    carlos=Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567890')
    print(estructuras)
    print(estructuras.contador_libros)