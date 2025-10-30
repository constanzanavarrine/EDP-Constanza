'''
Clase Anfibio


Vehículo que puede trasladarse por tierra o por agua (a motor).
Por defecto, trasladarse(desplazamiento: int) lo hace por tierra.
Implementa un método adicional para trasladarse por agua.

'''
from vehiculo import Vehiculo


class Anfibio(Vehiculo):
    _tipo_patente = "anfibio"

    def __init__(self, patente=None, *, marca=None, modelo=None):
        super().__init__(patente)
        self.marca = marca
        self.modelo = modelo
        self.modo_actual = "tierra"

    def trasladarse(self, desplazamiento: int) -> str:
        self.posicion += desplazamiento
        self.modo_actual = "tierra"
        return f"Anfibio avanza {desplazamiento} km por tierra."

    def trasladarse_por_agua(self, desplazamiento: int) -> str:
        self.posicion += desplazamiento
        self.modo_actual = "agua"
        return f"Anfibio navega {desplazamiento} km por agua."
