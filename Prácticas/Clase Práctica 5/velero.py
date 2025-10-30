from typing import Optional

from vehiculo import Vehiculo


class Velero(Vehiculo):
    """Vehiculo acuatico impulsado por velas.""" 

    _tipo_patente = "acuatico"

    def __init__(self, patente: Optional[str] = None, *, marca: str, anio: int, cantidad_velas: int):
        super().__init__(patente)
        self.marca = marca
        self.anio = anio
        self.cantidad_velas = cantidad_velas
        self.posicion_inicial = 0

    def trasladarse(self, desplazamiento: int) -> str:
        self.posicion += desplazamiento
        return f"Velero navega {desplazamiento} km por agua a vela."
