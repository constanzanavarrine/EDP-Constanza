"""
Clase Usuario para el Sistema de Gestión de Biblioteca
Representa un usuario
"""

from typing import List, Dict
from Libro import Libro


class Usuario:
    """
    Clase que representa un usuario de la biblioteca.

    Args:
        nombre (str): Nombre del usuario
        dni (str): DNI del usuario
    """

    def __init__(self, nombre: str, dni: str):
        """
        Constructor de la clase Usuario.

        Args:
            nombre (str): Nombre del usuario
            dni (str): DNI del usuario
        """
        self.__nombre = nombre
        self.__dni = dni
        self.__libros_prestados: Dict[str, Libro] = {}  # Diccionario {isbn: Libro} de libros prestados

    # Métodos getter
    def get_nombre(self) -> str:
        """
        Obtiene el nombre del usuario.

        Returns:
            str: Nombre del usuario
        """
        return self.__nombre



    def get_dni(self) -> str:
        """
        Obtiene el DNI del usuario.

        Returns:
            str: DNI del usuario
        """
        return self.__dni



    def get_libros_prestados(self) -> List[Libro]:
        """
        Obtiene la lista de libros actualmente prestados.

        Returns:
            List[Libro]: Lista de libros prestados (copia)
        """
        return list(self.__libros_prestados.values())



    # Métodos setter
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre del usuario.

        Args:
            nombre (str): Nuevo nombre del usuario
        """
        self.__nombre = nombre



    # Métodos de funcionalidad
    def pedir_libro_prestado(self, libro: Libro) -> None:
        """
        Solicita el préstamo de un libro.

        Args:
            libro (Libro): Libro a prestar

        Raises:
            ValueError: Si el usuario ya tiene este libro prestado o no se puede prestar
        """
        # Verificar que no tenga ya este libro prestado
        isbn = libro.get_isbn()
        if isbn in self.__libros_prestados:
            raise ValueError("El usuario ya tiene este libro prestado.")

        # Intentar prestar el libro
        try:
            libro.prestar()
            self.__libros_prestados[isbn] = libro
        except ValueError as e:
            raise ValueError(f"No se pudo prestar el libro: {e}")


    def devolver_libro_prestado(self, libro: Libro) -> None:
        """
        Devuelve un libro prestado.

        Args:
            libro (Libro): Libro a devolver

        Raises:
            ValueError: Si el usuario no tiene este libro prestado o no se puede devolver
        """
        isbn = libro.get_isbn()
        if isbn not in self.__libros_prestados:
            raise ValueError("El usuario no tiene este libro prestado.")

        # Intentar devolver el libro
        try:
            libro.devolver()
            del self.__libros_prestados[isbn]
        except ValueError as e:
            raise ValueError(f"No se pudo devolver el libro: {e}")



    def ver_libros_prestados(self) -> str:
        """
        Muestra los libros actualmente prestados.

        Returns:
            str: Representación de los libros prestados
        """
        if not self.__libros_prestados:
            return "No tienes libros prestados actualmente"



        # si el usuario se llama 'Ana'
        # Libros prestados - Ana
        libros = f"\nLibros Prestados - {self.__nombre}:\n"
        # "=================================================="
        libros += "=" * 50 + "\n"

        # self.__libros_prestados.values() -> devuelve todos los objetos
        # Libro prestados
        for libro in self.__libros_prestados.values():
            libros += f"{libro}\n"
                # f'{libro}' -> cuando ponemos el objeto dentro de 
                # un f-string, Python llama a su metodo __str__
                # Ejemplo: "1984 - Orwell (ISBN: 123)"
                
            libros += "-" * 50 + "\n"

        
        return libros  # devolvemos toda la cadena libros armada:
    
        '''
        Libros Prestados - Ana:
        ==================================================
        1984 - Orwell (ISBN: 123)
        --------------------------------------------------
        Fahrenheit 451 - Bradbury (ISBN: 456)
        --------------------------------------------------

        '''




    def __str__(self) -> str:
        """
        Representación en cadena del usuario.

        Returns:
            str: Representación del usuario
        """
        return f"{self.__nombre} (DNI: {self.__dni})"
