from typing import Optional

from vehiculo import Vehiculo


class Camion(Vehiculo):
    """Vehiculo terrestre con mayor numero de ruedas y capacidad de carga."""

    _tipo_patente = "terrestre"

    def __init__(self, patente: Optional[str] = None, *, marca: str, anio: int, capacidad_carga: float):
        super().__init__(patente)
        self.marca = marca
        self.anio = anio
        self.capacidad_carga = capacidad_carga
        self.ruedas = 8
        self.posicion_inicial = 0

    def trasladarse(self, desplazamiento: int) -> str:
        self.posicion += desplazamiento
        return f"Camion avanza {desplazamiento} km por tierra."
