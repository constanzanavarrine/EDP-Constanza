from collections import defaultdict
from itertools import count
from typing import Dict, Iterator, Set


class RegistroPatentes:
    
    """Administra las patentes ocupadas por tipo de vehiculo."""

    _ocupadas: Dict[str, Set[str]] = defaultdict(set)
    _contadores: Dict[str, Iterator[int]] = {}


    @classmethod
    def _normalizar_tipo(cls, tipo: str) -> str:
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("El tipo de vehiculo debe ser una cadena no vacia")
        
        return tipo.strip().lower()



    @classmethod
    def configurar_prefijo(cls, tipo: str, prefijo: str) -> None:
        
        """Permite fijar manualmente el prefijo que usara generar."""
        
        tipo_norm = cls._normalizar_tipo(tipo)
        
        if not isinstance(prefijo, str) or not prefijo.strip():
            raise ValueError("El prefijo debe ser una cadena no vacia")
        
        cls._prefijos[tipo_norm] = prefijo.strip().upper()



    _prefijos: Dict[str, str] = {}

    @classmethod
    def _prefijo_para(cls, tipo_norm: str) -> str:
        if tipo_norm in cls._prefijos:
            return cls._prefijos[tipo_norm]
        # Por defecto usa las primeras tres letras del tipo
        return tipo_norm[:3].upper()



    @classmethod
    def generar(cls, tipo: str) -> str:
        """Genera y reserva una nueva patente unica para el tipo dado."""
        tipo_norm = cls._normalizar_tipo(tipo)
        contador = cls._contadores.setdefault(tipo_norm, count(1))   # devuelve el valor de la clave
                                                                    # si no existe lo agrega con default 
        
        
        while True:
            secuencia = next(contador)
            patente = f"{cls._prefijo_para(tipo_norm)}-{secuencia:04d}"
            if patente not in cls._ocupadas[tipo_norm]:
                cls._ocupadas[tipo_norm].add(patente)
                return patente



    @classmethod
    def registrar(cls, tipo: str, patente: str) -> str:
        """Reserva una patente provista por el usuario para el tipo indicado."""
        
        tipo_norm = cls._normalizar_tipo(tipo)
        
        if not isinstance(patente, str) or not patente.strip():
            raise ValueError("La patente debe ser una cadena no vacia")
        
        patente_norm = patente.strip().upper()
        
        if patente_norm in cls._ocupadas[tipo_norm]:
            raise ValueError(
                f"La patente '{patente_norm}' ya esta asignada al tipo '{tipo_norm}'."
            )
        cls._ocupadas[tipo_norm].add(patente_norm)
        
        return patente_norm




    @classmethod
    def liberar(cls, tipo: str, patente: str) -> None:
        """Libera una patente previamente asignada."""
        
        tipo_norm = cls._normalizar_tipo(tipo)
        
        cls._ocupadas[tipo_norm].discard(patente.strip().upper())




    @classmethod
    def esta_ocupada(cls, tipo: str, patente: str) -> bool:
        
        tipo_norm = cls._normalizar_tipo(tipo)
        
        return patente.strip().upper() in cls._ocupadas[tipo_norm]
