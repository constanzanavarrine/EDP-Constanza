import csv
import random 
from typing import Any, Dict

class ValidationError(Exception):
    '''Excepcion personalizada para errores de validacion'''
    pass


class Validador: 
    @classmethod
    def validar_entero(cls, valor: Any, nombre_campo: str = 'Campo') -> int:
        '''Valida que el valor sea un entero valido. Retorna el entero si es valido.'''
        # Evitar que bool pase como int
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValidationError(f'{nombre_campo} debe ser un entero valido. Valor recibido {valor}')
        return int(valor)

    @classmethod
    def validar_string(cls, valor: Any, nombre_campo: str = 'Campo') -> str:
        '''Valida que el valor sea un string valido. Retorna el str si es valido'''
        if not isinstance(valor, str):
            raise ValidationError(f'{nombre_campo} debe ser un string válido. Valor recibido {valor}')
        s = valor.strip()
        if not s:
            raise ValidationError(f'{nombre_campo} no puede estar vacío.')
        return s
    


class Producto: 
    def __init__(self, titulo: str, artista: str, anio_lanzamiento: int, cod_barras: str): 
        self.titulo = self.valido_titulo(titulo)
        self.artista = self.valido_artista(artista)
        self.anio_lanzamiento = self.valido_anio(anio_lanzamiento)
        self.cod_barras = self.valido_cod_barras(cod_barras)
  
    @staticmethod
    def _validar_ean13(codigo: str) -> bool:
        if not isinstance(codigo, str) or len(codigo) != 13 or not codigo.isdigit():
            return False
        # pesos 1,3 alternados sobre los primeros 12 dígitos
        suma = sum((3 if i % 2 else 1) * int(d) for i, d in enumerate(codigo[:-1]))
        dv = (10 - (suma % 10)) % 10
        return dv == int(codigo[-1])
  
    # valido que el titulo sea un str
    def valido_titulo(self, valor: Any) -> str:
        return Validador.validar_string(valor, nombre_campo='Titulo')
  
    # valido que el artista sea un str y no contenga numeros
    # permitimos espacios (y letras con acentos)
    def valido_artista(self, valor: Any) -> str:
        arts = Validador.validar_string(valor, nombre_campo='Artista')
        solo_letras = arts.replace(' ', '')
        if not solo_letras.isalpha():
            raise TypeError('El nombre del artista solo debe contener letras y espacios.')
        return arts
  
    def valido_anio(self, valor: Any) -> int:
        anio = Validador.validar_entero(valor, nombre_campo='Año de lanzamiento')
        if anio < 1877 or anio > 2100:
            raise ValueError('Año de lanzamiento fuera de rango razonable (1877–2100).')
        return anio
  
    def valido_cod_barras(self, codigo: Any) -> str:
        codigo_str = Validador.validar_string(codigo, nombre_campo='Código de barras')
        if not self._validar_ean13(codigo_str):
            raise ValidationError('Código de barras EAN-13 inválido.')
        return codigo_str
  
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(titulo='{self.titulo}', artista='{self.artista}', "
                f"año={self.anio_lanzamiento}, ean13={self.cod_barras})")
  


class Cd(Producto):
    def __init__(self, titulo: str, artista: str, anio_lanzamiento: int, cod_barras: str, duracion: int):
        super().__init__(titulo, artista, anio_lanzamiento, cod_barras)
        self.duracion = self.validar_duracion(duracion)
    
    # valido que la duracion sea un entero positivo
    def validar_duracion(self, valor: Any) -> int: 
        valor = Validador.validar_entero(valor, nombre_campo='Duracion')
        if valor < 0:
            raise ValueError('La duracion debe ser positiva')
        return valor
  
    def __repr__(self) -> str:
        base = super().__repr__()[:-1]  # quitar último ')'
        return f"{base}, duracion={self.duracion})"




class Vinilo(Producto):
    def __init__(self, titulo: str, artista: str, anio_lanzamiento: int, cod_barras: str, diametro: int):
        super().__init__(titulo, artista, anio_lanzamiento, cod_barras)
        self.diametro = self.validar_vinilo(diametro)
  
    # valido que el diametro sea un entero positivo
    def validar_vinilo(self, valor: Any) -> int: 
        valor = Validador.validar_entero(valor, nombre_campo='Vinilo')
        if valor <= 0:
            raise ValueError('El diametro del vinilo debe ser positivo')
        return valor
  
    def __repr__(self) -> str:
        base = super().__repr__()[:-1]
        return f"{base}, diametro={self.diametro})"
    


class Tienda:
    def __init__(self, nombre: str): 
        self.nombre = Validador.validar_string(nombre, nombre_campo='Nombre de tienda')
        self.tienda_por_productos: Dict[str, Producto] = {}
  
    def agregar_prod(self, producto: Producto) -> None:
        '''Agrega el producto si su codigo no existe aun y verifica que 
        el producto por parametro sea de la clase Producto'''
        if not isinstance(producto, Producto):
            raise ValidationError('El ingreso no corresponde a un valor del tipo Producto')
        codigo = producto.cod_barras
        if codigo in self.tienda_por_productos:
            print('El producto que intenta agregar ya se encuentra en la tienda')
            return 
        self.tienda_por_productos[codigo] = producto 
        print('El producto ha sido agregado con exito')
      
    def eliminar_prod_por_codigo(self, codigo: str) -> None:
        '''eliminar producto por código (valida que exista)'''
        codigo = Validador.validar_string(codigo, nombre_campo='Código')
        if codigo not in self.tienda_por_productos:
            print('No se encontro un producto con ese codigo')
            return 
        del self.tienda_por_productos[codigo]
        print('Producto eliminado')
    
    def buscar_prod(self, codigo: str):
        '''Busca un producto por su código. Devuelve Producto o None.'''
        codigo = Validador.validar_string(codigo, nombre_campo='Código')
        return self.tienda_por_productos.get(codigo)
  
    def mostrar_prod(self):
        d = self.tienda_por_productos
        for producto in sorted(d.values(), key=lambda x: x.anio_lanzamiento):
            print(producto)
  
    def guardar_csv(self, ruta_archivo: str) -> None:
        """
        Guarda todo el inventario en un CSV con columnas:
        ["Título", "Artista", "Año", "Tipo", "Atributo Adicional", "Código"].

        Lanza ValidationError con un mensaje claro si no puede guardar.
        """
        columnas = ["Título", "Artista", "Año", "Tipo", "Atributo Adicional", "Código"]

        # Validación simple de ruta
        ruta = Validador.validar_string(ruta_archivo, nombre_campo="Ruta de archivo")

        try:
            with open(ruta, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=columnas)
                writer.writeheader()

                for prod in self.tienda_por_productos.values():
                    if isinstance(prod, Cd):
                        tipo = "Cd"
                        atributo = f"Duración: {prod.duracion}"
                    elif isinstance(prod, Vinilo):
                        tipo = "Vinilo"
                        atributo = f"Diámetro: {prod.diametro}"
                    else:
                        # Por si en el futuro agregás otros tipos
                        tipo = prod.__class__.__name__
                        atributo = ""

                    fila = {
                        "Título": prod.titulo,
                        "Artista": prod.artista,
                        "Año": prod.anio_lanzamiento,
                        "Tipo": tipo,
                        "Atributo Adicional": atributo,
                        "Código": prod.cod_barras,
                    }
                    writer.writerow(fila)

        except OSError as e:
            # Problemas de E/S (permisos, carpeta inexistente, etc.)
            raise ValidationError(f"No se pudo guardar el CSV en '{ruta}': {e}")

        # Validación extra: si el archivo quedó vacío (por ejemplo, tienda vacía)
        if not self.tienda_por_productos:
            # No rompemos el archivo, pero avisamos que no había datos
            raise ValidationError("Se generó el CSV pero la tienda no tenía productos (archivo con solo encabezado).")

        


def main():
    try:
        # EAN-13 válidos de ejemplo
        ean1 = '4006381333931'  # ejemplo típico
        ean2 = '5901234123457'  # ejemplo estándar EAN-13
        ean3 = '9780306406157'  # ISBN-13 válido (prefijo de libros)

        producto1 = Cd('The Beatles 1', 'The Beatles', 2000, ean1, 79)
        producto2 = Vinilo('Random Access Memories', 'Daft Punk', 2013, ean2, 12)
        producto3 = Cd('Midnights', 'Taylor Swift', 2022, ean3, 61)

        tienda = Tienda('Tienda de Música')
        tienda.agregar_prod(producto1)
        tienda.agregar_prod(producto2)
        tienda.agregar_prod(producto3)

        print('\nInventario ordenado por año:')
        tienda.mostrar_prod()

        print('\nBuscar uno:')
        encontrado = tienda.buscar_prod(ean2)
        print('Encontrado:', encontrado)

        print('\nEliminar uno:')
        tienda.eliminar_prod_por_codigo(ean2)

        print('\nInventario final:')
        tienda.mostrar_prod()

        tienda.guardar_csv("inventario.csv")

    except (ValidationError, TypeError, ValueError) as e:
        print('Error:', e)


if __name__ == '__main__':
    main()



















