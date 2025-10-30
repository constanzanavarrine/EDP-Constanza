from typing import Optional

from vehiculo import Vehiculo


class Lancha(Vehiculo):
    """Vehiculo acuatico propulsado a motor."""

    _tipo_patente = "acuatico"

    def __init__(self, patente: Optional[str] = None, *, marca: str, anio: int, marca_motor: str):
        super().__init__(patente)
        self.marca = marca
        self.anio = anio
        self.marca_motor = marca_motor
        self.posicion_inicial = 0

    def trasladarse(self, desplazamiento: int) -> str:
        self.posicion += desplazamiento
        return f"Lancha navega {desplazamiento} km por agua a motor."
