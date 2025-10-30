
from __future__ import annotations
from math import isqrt
from typing import Any, Dict, List



class ValidationError(Exception):
  '''Excepcion personalizada para errores de validacion'''

  pass



class Validador: 
  
  @classmethod
  def validar_entero(cls, valor: Any, nombre_campo: str = 'Campo') -> int:
    '''Valida que el valor sea un entero valido.
    Retorna el entero si es valido. '''
    if not isinstance(valor, int):
      raise ValidationError(f'{nombre_campo} debe ser un entero valido. Valor recibido '{valor}'')
    
    return int(valor)



class NumberBlock: 
  
  # atributos de clase = globales para TODOS los Numberblock 
  colores_validos: List[str] = ['violeta', 'rojo', 'naranja', 'amarillo', 'verde']
  
  registro: Dict[int, List[NumberBlock]] = {}
  
  
  # constructor 
  def __init__(self, valor: int, color: str, atributos_personalidad: list):
  
    self.valor = self.validar_valor(valor)
    self.color = self.validar_color(color)
    self.atributos_personalidad = self.validar_personalidad(atributos_personalidad)
    
    
    # Agregamos Numberblock al registro
    
    self.registrar_nb(self)
  
  def validar_valor(self, valor: int) -> int: 
    valor = Validador.validar_entero(valor, nombre_campo = 'Valor NB')
    
    if valor < 0:
      raise ValueError('El valor del Numberblock debe ser positivo')
  
    # Todo validado: retorno el entero positivo 
    return valor
    
    
  def validar_color(self, color: str) -> str:
    if color not in NumberBlock.colores_validos:
      #Invalido si NO esta en la lista de colores validos 
      raise ValueError('Color invalido.')
    
    # Todo valido: retorno la string
    return color 
  

  
  def validar_personalidad(self, personalidad: lits) -> list:
    if not isinstance(personalidad,list):
      raise ValueError('Personalidad debe tener al menos un atributo')
    
    if not personalidad:
      raise ValueError('Personalidad debe tener al menos un atributo')
  
    # Todo validado: retorno la lista
  
  
  
  def registrar_nb(self, nb: NumberBlock):
    if not isinstance(nb, NumberBlock):
      raise TypeError('Error en registrar_nb: el nb pasado por parametro no es de tipo NumberBlock')
  
    # Extraigo el numero del Numberblock a registrar
    numero = nb.valor
    if numero not in self.registro: 
      self.registro[numero] = []
    
    # Agrego la lista al objeto Numberblock
    self.registro[numero].append(nb)
  
  
  
  def es_perfecto(self) -> bool:
    raiz_entera = isqrt(self.valor)
    
    # Retorno True si el resultado de elevar al cuadrado la raiz cuadrada
    # entera y el valor original son iguales
    
    return raiz_entera**2 == self.valor
  
  
  
  def replicar(self) -> NumberBlock:
    return NumberBlock(self.valor, self.color, self.atributos_personalidad)
  
  
  
  def combinar_con(self, other: NumberBlock) -> NumberBlock:
    if not isinstance(other, NumberBlock):
      raise TypeError(f'No se puede combinar. Tipo '{type(other)}' invalido')
  
    suma = self.valor + other.valor
    
    if suma not in NumberBlock.registro:
      # construyo un numberblock nuevo
      resultado = NumberBlock(suma, self.color, other.atributos_personalidad)


    else:
      # reutilizo el primer valor de los Numberblocks existentes con ese numero
      resultado = NumberBlock.registro[suma][0]
      
      '''registro = {
    3: [nb3],
    4: [nb4],
    7: [nb7_original, nb7_original]  # misma instancia repetida en la lista
    }
    si suma = 7  --> suma[7] = [nb7_original, nb7_original] -> suma[7][0] = nb7_original
    '''
      
      # lo registro en el diccionario:
      self.registrar_nb(resultado)
    '''como es una replica mas la tenemos que volver a registrar para contar
    "mas replicas"'''
      
    
    return resultado 
    
    
  
  def personalidad(self) -> None:
    ''' Recorre la lista self.atributos_personalidad 
    (los rasgos de personalidad que le diste al Numberblock).
    Imprime cada rasgo uno por uno en una línea distinta.'''
    
    for attr in self.atributos_personalidad:
      print(attr)
    


  @classmethod
  def personajes(cls) -> None:
    personajes_ordenados = dict(sorted(cls.registro.items(())))
    
    '''2. sorted(...)

            sorted(cls.registro.items()) ordena esa lista de tuplas por la clave numérica (porque la clave 
            es el primer elemento de cada tupla).

            Resultado:

            [(3, [nb3, nb3_replica]), (4, [nb4]), (7, [nb7, nb7, nb7])]


            (En este caso ya estaba ordenado, pero si no lo estuviera, 
            acá se asegura de que quede en orden ascendente de número).

    3  . dict(sorted(...))

            Convierte la lista de tuplas de nuevo en un diccionario ordenado por clave:

        {
            3: [nb3, nb3_replica],
            4: [nb4],
            7: [nb7, nb7, nb7]
            '''
    
    for numero in personajes_ordenados: 
        replicas_nb = personajes_ordenados[numero]
        nb_original = replicas_nb[0]
        print(f'#{numero}: "{nb_original}" - Replicas: {len(replicas_nb)}')
    
    '''4. for numero in personajes_ordenados:

        Cuando iterás un diccionario, Python recorre las claves (3, 4, 7).

        5. replicas_nb = personajes_ordenados[numero]

        Para cada número, toma la lista de instancias registradas:

        replicas_nb = [nb3, nb3_replica] si el número es 3, por ejemplo.

        6. nb_original = replicas_nb[0]

        El primer elemento de la lista es considerado el Numberblock original 
        (los demás son réplicas o combinaciones).
        
    '''
      

    def __repr__(self) -> str:
        presentacion = f'Soy el numero {self.valor}, soy {self.color}'
        if self.es_perfecto():
            presentacion += 'Soy un cuadrado perfecto.'
        
        return presentacion


    
    def __eq__(self, other: NumberBlock):
        "Método necesario para establecer la igualdad de las réplicas"
        if not isinstance(other, NumberBlock):
            return False

        valores_iguales = self.valor == other.valor
        colores_iguales = self.color == other.color
        personalidades_iguales = set(self.atributos_personalidad) == set(other.atributos_personalidad)

        return valores_iguales and colores_iguales and personalidades_iguales


class Rebelblock(NumberBlock):
    def __init__(self, valor: int, color: str, personalidad: list):
        self.valor = self.validar_valor(valor)
        if self.valor in self.registro:
            raise ValueError("Este Rebelblock ya existe")
        self.color = self.validar_color(color)
        self.atributos = self.validar_personalidad(personalidad)

        # Agregamos Rebelblock al registro
        self.registrar_nb(self)

    def validar_valor(self, valor: int) -> int:
        valor = Validador.validar_entero(valor, nombre_campo="Valor RB")
        if valor >= 0:
            raise ValueError("El valor del Rebelblock debe ser negativo")

        # Todo validado:
        return valor

    def validar_color(self, color: str) -> str:
        if color in Rebelblock.colores_validos:
            raise ValueError("Color inválido.")

        # Todo validado:
        return color

    def replicar(self) -> None:
        print("No me replico, no insistas.")

    def combinar_con(self, other) -> None:
        print("No quiero combinarme!")

    def __repr__(self):
        return f"Soy {self.valor}, y me jacto de ser negativo."




def prueba_1():
    nb_1 = NumberBlock(1, "rojo", ["lindo", "amable"])
    nb_1_rep = nb_1.replicar()

    print(nb_1 == nb_1_rep)

    NumberBlock.personajes()


def prueba_2():
    nb_invalido = NumberBlock(1.14, "rojo", ["lindo", "amable"])


def prueba_3():
    nb_3 = NumberBlock(3, "amarillo", ["curioso", "entusiasta"])
    nb_4 = NumberBlock(4, "verde", ["amable", "bueno"])

    nb_7 = nb_3.combinar_con(nb_4)

    NumberBlock.personajes()

    nb_7.personalidad()


def prueba_4():
    nb_7 = NumberBlock(7, "naranja", ["honrado"])

    nb_3 = NumberBlock(3, "amarillo", ["curioso", "entusiasta"])
    nb_4 = NumberBlock(4, "verde", ["amable", "bueno"])

    nb_7_comb = nb_3.combinar_con(nb_4)

    NumberBlock.personajes()

    nb_7_comb.personalidad()


def prueba_5():
    rb_invalido = Rebelblock(1, "violeta", ["maquiavelico"])


def prueba_6():
    rebelblock = Rebelblock(-1, "negro", ["triste"])
    rebelblock.replicar()

    Rebelblock.personajes()


if __name__ == "__main__":
    prueba_6()
