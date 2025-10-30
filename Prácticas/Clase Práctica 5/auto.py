from typing import Optional

from vehiculo import Vehiculo


class Auto(Vehiculo):
    """Vehiculo terrestre con cuatro ruedas."""

    _tipo_patente = "terrestre"

    def __init__(self, patente: Optional[str] = None, *, marca: str, anio: int):
        super().__init__(patente)
        self.marca = marca
        self.anio = anio
        self.ruedas = 4
        self.posicion_inicial = 0

    def trasladarse(self, desplazamiento: int) -> str:
        self.posicion += desplazamiento
        return f"Auto avanza {desplazamiento} km por tierra."
