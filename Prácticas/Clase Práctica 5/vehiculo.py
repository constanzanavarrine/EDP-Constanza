from typing import Optional

from registro_patentes import RegistroPatentes


class Vehiculo:
    "Base comun: todos tienen patente y posicion"

    _tipo_patente: Optional[str] = None

    def __init__(self, patente: Optional[str] = None):
        
        tipo = self._obtener_tipo_patente()
        
        if patente is None:
            self.patente = RegistroPatentes.generar(tipo)
        else:
            self.patente = RegistroPatentes.registrar(tipo, patente)
            
        self.posicion = 0  # por defecto todos tienen posicion 0


    def _obtener_tipo_patente(self) -> str:
        '''
        getattr(self, "_tipo_patente", None) para preguntar “¿la instancia 
        (o su clase) tiene un _tipo_patente definido?”. Si está, lo devuelve; si no, 
        retorna None y puedo detectar el caso para lanzar el ValueError con un mensaje 
        más claro
        '''
        
        
        tipo = getattr(self, "_tipo_patente", None)
        
        if not tipo:
            raise ValueError(
                "La subclase de Vehiculo debe definir _tipo_patente (ej. 'terrestre' o 'acuatico')."
            )
        return tipo


    def __eq__(self, other) -> bool:
        if not isinstance(other, Vehiculo):
            return False
        
        return (
            self.patente == other.patente
            and self._obtener_tipo_patente() == other._obtener_tipo_patente()
        )


    def __hash__(self) -> int:
        return hash((self._obtener_tipo_patente(), self.patente))



    def trasladarse(self, desplazamiento: int) -> str:
        
        # Si creamos un objeto directamente en la clase base y tratamos de llamarla
        # desde nuestra clase Vehiculo, entonces transladarse explota aca

        raise NotImplementedError('Cada subclase define su propio metodo de traslado.')
