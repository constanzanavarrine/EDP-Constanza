# Modulo de validacion 

# validador_entrada.py

class ValidadorEntrada:
    
    '''Funciones puras de validacion: reciben valores, devuelven valores limpios
    o lanzan ValueError
    
    '''

    # @staticmethod -> no depende del estado interno
    
    @staticmethod
    def anio(anio_str: str, anios_disponibles | None = None) -> str:
        
        '''Valida que sea un anio de 4 digitos. Opcional: que exista en el dataset.
        '''
        
        if not isinstance(anio_str, str):
            raise ValueError('El anio debe ser una cadena.')
        
        anio = anio_str.strip()
        
        if not (anio.isdigit() and len(anio) == 4):
            raise ValueError('Anio invalido: debe tener 4 digitos.')
        
        if anios_disponibles is not None and anio not in anios_disponibles:
            raise ValueError(f'No hay registros para el anio {anio}')
        
        return anio
    
    @staticmethod
    def mes(mes_str: str) -> int:
        '''Valida mes 1..12 y lo devuelve como int'''
        if not isinstance(mes_str, str):
            raise ValueError('El mes debe ser una cadena.')
        mes_s = mes_str.strip()
        
        if not (mes_s.isdigit() and 1<= int(mes_s) <=12):
            raise ValueError('Mes invalido: debe estar entre 1 y 12')
        
        return int(mes_s)

    @staticmethod
    def transporte(transporte: str, transportes_validos) -> str:
        '''Valida que el transporte exista en el conjunto permitido
        (coincidencia exacta, case-insensititive opcional)'''     
        
        if not isinstance(transporte,str):
            raise ValueError('El transporte debe ser cadena.')
        
        t = transporte.strip()
        
        if t not in transportes_validos:
            # Case- insensitive: if t.lower() not in {x.lower() for x in transportes validos}:
            raise ValueError (f'Transporte invalido: {t}.Validos: {sorted(transportes_validos)}')
        
        return t
               
        