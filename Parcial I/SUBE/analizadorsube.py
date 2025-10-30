# Analizador -> recibe valores YA validados

from typing import Iterable, Dict, List, Any

class AnalizadorSube:
    
    '''Clase de negocio: guarda datos y hace analisis. No pide input al usuario ni imprime 
    errores: eso va fuera
    '''
    
    def __init__(self, datos: List[Dict[str,Any]]):
        # datos: lista de dicts, p.ej  [{'indice_tiempo':'2020-01-01','lancha':'40',...}, ...]
        self.datos = datos
        
        # derivados utiles: conjuntos de anios y transportes disponibles
        self.anios_disponibles = self._extraer_anios()
        self.transportes_disponibles = self._extraer_transportes()
        
        def _extraer_anios(self) -> set[str]:
            anios = set()
            for fila in self.datos:
                fecha = fila.get('indice_tiempo','')
                anio = fecha.split('-')[0] if fecha else ''
                if anio.isdigit() and len(anio) == 4:
                    anios.add(anio)
            
            return anios 
                


    def _extraer_transportes(self) -> set[str]:
        
        # Todas las columnas excepto las de tiempo/total las consideramos 'transportes'
        if not self.datos:
            return set()
        
        # para saber cuales son las claves, alcanza con mirar la primera fila → self.datos[0]
            # nos sirve por si llegamos a agregar mas medios de transporte 
        ejemplo = set(self.datos[0].keys()) # → tomo todas las columnas de una fila.
        
        return {c for c in ejemplo if c not in {'indice_tiempo','total'}} # → filtro solo las que corresponden a transportes.
    
    
    # Ejemplo: medio mas usado en (anio,mes) dados (YA validados)
    def medio_mas_usado_mes(self, anio: str, mes: int) -> tuple[str,int]:
        
        # Filtrar filas del anio y mes
        mes_str = f'{mes:02d}'  # -> casteamos el mes porque el CSV viene con un cero delante del mes 
        
        filtradas = list(filter(lambda f: f["indice_tiempo"].startswith(f"{anio}-{mes_str}-"), self.datos))

                     
        # Agregar por trasnporte 
        totales: Dict[str, int] = {t: 0 for t in self.trasportes_disponibles}
        # Crea un diccionario como {"colectivo": 0, "tren": 0, "lancha": 0, ...}.
    
        
        
        for f in filtradas:
            for t in self.transportes_disponibles:
                # Los CSV suelen tener strings, casteamos a int cuidando vacios 
                
                try: 
                    totales[t] += int(f.get(t,0) or 0)
                except ValueError:
                    pass
                
                    '''Recorre cada fila del mes.

                        Por cada transporte t, agarra f[t] (ej. "907421") y lo convierte a entero.

                        Lo suma al acumulador en totales[t].

                        Usa try/except por si algún valor está vacío o mal formateado.'''
        
        
        # Elegir el maximo 
        if not filtradas:
            return ('(sin datos)',0)
        
        medio, usuarios = max(totales.items(), key = lambda kv: kv[1])
        return medio, usuarios 
    
    
        '''
        totales.items()
        .items(), obtenés una vista de pares (clave, valor)
        {
  "colectivo": 3564004,
  "lancha": 94,
  "subte": 511136,
  "tren": 719721
}

        ¿Qué hace max(...) normalmente?
        Si aplicás max directamente sobre esa lista, 
        Python va a intentar comparar las tuplas completas: 
        primero la clave, después el valor. Eso no es lo que queremos.
        
        
        Qué significa key=... en max?

        El parámetro key sirve para decirle a max qué 
        criterio usar para decidir cuál es “más grande”.
        
        
        Qué hace lambda kv: kv[1]?

        lambda kv: kv[1] es una función anónima que 
        recibe una tupla (clave, valor) y devuelve el valor (posición 1).

        En este caso:

        Para ("colectivo", 3564004) devuelve 3564004.

        Para ("lancha", 94) devuelve 94.

        etc.

        Entonces max(..., key=lambda kv: kv[1]) significa:
        👉 “De todos los pares (medio, usuarios),
        elegí el que tenga más usuarios”.
        
        medio, usuarios = ... desempaqueta la tupla ganadora:
        
        
        '''
        