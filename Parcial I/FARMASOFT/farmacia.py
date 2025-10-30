import csv
from typing import Dict, List, Any
from datetime import date, timedelta

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

# ---------- util para EAN-13 ----------
def ean13_checksum(d12: str) -> int:
    """Recibe 12 dígitos y devuelve el dígito verificador."""
    if len(d12) != 12 or not d12.isdigit():
        raise ValueError("Se esperan exactamente 12 dígitos para calcular el EAN-13.")
    suma = sum((3 if i % 2 else 1) * int(d) for i, d in enumerate(d12))
    return (10 - (suma % 10)) % 10

def make_ean13(d12: str) -> str:
    """Arma un EAN-13 válido a partir de 12 dígitos."""
    return d12 + str(ean13_checksum(d12))


class Medicamentos:
  
  # constructor
  def __init__(self, nombre: str, lab: str, cod_barras: int, vence: str):
    self.nombre = self.valido_nombre(nombre)
    self.lab = self.valido_lab(lab)
    self.cod_barras = self.valido_codigo_barras(cod_barras)
    self.vence = self.valido_fecha_vencimiento(vence) 
  
  # valido ingreso nombre medicamento
  def valido_nombre(self, valor: str) -> str:
    return Validador.validar_string(valor, nombre_campo = 'Nombre medicamento')
  
  # valido ingreso laboratorio
  def valido_lab(self, valor:str) -> str:
    return Validador.validar_string(valor, nombre_campo = 'Laboratorio')
  
  
  # valido codigo barras (EAN-13), retorno el string si es válido o levanto error
  @staticmethod
  def _es_ean13(codigo: str) -> bool:
      if len(codigo) != 13 or not codigo.isdigit():
          return False
      # pesos 1,3 alternados en los primeros 12 dígitos
      suma = sum((3 if i % 2 else 1) * int(d) for i, d in enumerate(codigo[:-1]))
      dv = (10 - (suma % 10)) % 10
      return dv == int(codigo[-1])

  def valido_codigo_barras(self, codigo: Any) -> str:
      s = Validador.validar_string(codigo, nombre_campo='Código de barras')
      if not self._es_ean13(s):
          raise ValidationError('Código de barras EAN-13 inválido.')
      return s
  
  
  # valido fecha de vencimiento (formato yyyy-mm-dd)
  def valido_fecha_vencimiento(self, valor:str) -> date:
    s = Validador.validar_string(valor, nombre_campo='Fecha vencimiento')
    try:
        # Acepta estrictamente 'YYYY-MM-DD'
        fecha = date.fromisoformat(s)      # levanta ValueError si no existe o mal formado
    
    except ValueError:
        raise ValidationError("Fecha de vencimiento inválida. Use el formato YYYY-MM-DD (ej: 2025-12-31).")

    # Requisito típico: que sea futura
    if fecha <= date.today():
        raise ValidationError("La fecha de vencimiento debe ser futura.")
    return fecha
  
  
  
  def __repr__(self) -> str:
    return (f'{self.__class__.__name__}: {self.nombre} | Lab: {self.lab} | Vence: {self.vence} |')
    
    
    

class MedicamentoReceta(Medicamentos):
  # constructor 
  def __init__(self, nombre: str, lab: str, cod_barras: int, vence: str, registro: str):
    super().__init__(nombre, lab, cod_barras, vence)
    
    self.registro = self.valido_registro(registro)
  
  def valido_registro(self, valor :str):
    '''valida que sea un dato tipo str alfanumerico con minimo 8 caracteres'''
    rs = Validador.validar_string(valor, nombre_campo = 'Registro sanitario')
    
    if len(rs) < 8: 
      raise Exception('El registro ingresado es incorrecto, debe contener como minimo 8 caracteres. ')
  
    if not rs.isalnum():
      raise Exception('El registro ingresado es incorrecto, el tipo de dato no es valido. ')
    
    return rs
  

  def __repr__(self) -> str:
    base = super().__repr__()
    return f'{base} Registro: {self.registro} | Codigo: {self.cod_barras}'
  
  

class MedicamentoVL(Medicamentos):
  def __init__(self, nombre: str, lab: str, cod_barras: int, vence: str, dosis: str):
    super().__init__(nombre, lab, cod_barras, vence)
    self.dosis = self.validar_dosis(dosis)
    
  def validar_dosis(self, valor: str):
    return Validador.validar_string(valor, nombre_campo = 'Dosis')
  
  def __repr__(self) -> str:
    base = super().__repr__()
    return f'{base} Dosis: {self.dosis} | Codigo: {self.cod_barras}'
    


class Farmacia: 
  
  def __init__(self,nombre):
    self.nombre = self.valido_nombre_farmacia(nombre)
    self.medicamentos_unicos: Dict[str,medicamento] = {}
  
  def valido_nombre_farmacia(self, nombre: str):
    return Validador.validar_string(nombre, nombre_campo = 'Farmacia')
  
  def agregar_medicamento(self, medicamento: Medicamentos) -> None:
    '''suma un medicamento a la farmacia 
    -> no pueden haber dos medicamentos con el mismo codigo de barras'''
    
    if not isinstance(medicamento, Medicamentos):
      raise ValidationError('El objeto que intenta agregar no es del tipo medicamento')
    
    cod = medicamento.cod_barras
    if cod not in self.medicamentos_unicos:
      self.medicamentos_unicos[cod] = medicamento
      print('El medicamento ha sido agregado con exito')
    
    else: 
      print('El codigo de medicamento que intenta agregar ya se encuentra asociado en la farmacia. ')
      

  def eliminar_medicamentos(self, codigo: str) -> None:
    '''elimina un medicamento a partir del codigo de barras'''
    codigo = valido_codigo_barras(codigo)
    if codigo not in self.medicamentos_unicos:
      print('El medicamento que intenta eliminar no se encuentra en la farmacia')
    
    del self.medicamentos_unicos[codigo]
    print('Producto eliminado')
  
  
  def mostrar_medicamentos(self) -> None:
  
    if not self.medicamentos_unicos:
      print('no hay medicamentos en el inventario')
      return
    else:
      d = self.medicamentos_unicos
      for med in sorted(d.values(), key = lambda x: x.vence):
        print(f'- {med}')
    
  def alerta_vencimientos(self, dias: int = 30):
    # 1) validar param
    dias = Validador.validar_entero(dias, nombre_campo="Días")
    if dias < 0:
        raise ValidationError("La cantidad de días no puede ser negativa.")

    # 2) rango
    hoy = date.today()
    fecha_limite = hoy + timedelta(days=dias)

    # 3) filtrar SOLO objetos cuyo .vence es date y está en el rango [hoy, limite]
    vencen = list(filter(lambda m: isinstance(m.vence, date) and (hoy <= m.vence <= fecha_limite),
                         self.medicamentos_unicos.values()))

    # 4) si está vacío, mensaje y retorno
    if not vencen:
        print(f"No hay medicamentos que venzan en los próximos {dias} días.")
        return []

    # 5) ordenar e imprimir
    vencen.sort(key=lambda m: m.vence)
    print(f"Medicamentos que se vencen en los próximos {dias} días (hasta {fecha_limite}):")
    for med in vencen:
        dias_rest = (med.vence - hoy).days
        print(f"- {med} (vence: {med.vence}, en {dias_rest} día(s))")

    return vencen


  def guardar_csv(self, ruta_archivo: str) -> None:
      """
      Guarda todo el inventario en un CSV con columnas:
      ["Nombre", "Laboratorio", "Fecha de Vencimiento", "Tipo", "Registro Sanitario", "Dosis recomendada"].

      Lanza ValidationError con un mensaje claro si no puede guardar.
      """
      
      columnas = ["Nombre", "Laboratorio", "Fecha de Vencimiento", "Tipo", "Registro Sanitario", "Dosis recomendada"]

      # Validación simple de ruta
      ruta = Validador.validar_string(ruta_archivo, nombre_campo="Ruta de archivo")

      try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
          writer = csv.DictWriter(f, fieldnames=columnas)
          writer.writeheader()
            
          for med in self.medicamentos_unicos.values():
                if isinstance(med, MedicamentoReceta):
                    tipo = "Receta"
                    registro_sanitario = med.registro
                    dosis_recomendada = "No tiene"
                elif isinstance(med, MedicamentoVL):
                    tipo = "Venta Libre"
                    registro_sanitario = "No tiene"
                    dosis_recomendada = med.dosis
                else:
                    tipo = med.__class__.__name__
                    registro_sanitario = ""
                    dosis_recomendada = ""

                fila = {
                    "Nombre": med.nombre,
                    "Laboratorio": med.lab,
                    "Fecha de Vencimiento": (
                        med.vence.isoformat() if isinstance(med.vence, date) else str(med.vence)
                    ),
                    "Tipo": tipo,
                    "Registro Sanitario": registro_sanitario,
                    "Dosis recomendada": dosis_recomendada,
                }
                writer.writerow(fila)

      except OSError as e:
          # Problemas de E/S (permisos, carpeta inexistente, etc.)
          raise ValidationError(f"No se pudo guardar el CSV en '{ruta}': {e}")

      # Validación extra: si el archivo quedó vacío (por ejemplo, tienda vacía)
      if not self.medicamentos_unicos:
          # No rompemos el archivo, pero avisamos que no había datos
          raise ValidationError("Se generó el CSV pero la tienda no tenía productos (archivo con solo encabezado).")

    
def main():
  try:
    
    farmacia = Farmacia('Farmacity')

    ean_ok1 = '4006381333931'              # ejemplo conocido válido
    ean_ok2 = make_ean13('400638122393')   # genera uno válido a partir de 12 dígitos
    ean_ok3 = make_ean13('590123412345')   # otro válido
    ean_ok4 = make_ean13('590193412345')
    
    medicamento1 = MedicamentoReceta('Ibuprofeno', 'Bayer', ean_ok1, '2026-12-14', 'ttiejdu898')
    medicamento2 = MedicamentoReceta('Actron', 'Bayer', ean_ok2, '2026-10-10', 'ttiejdu778')
    medicamento3 = MedicamentoReceta('Certal', 'Bayer', ean_ok3, '2026-10-08', 'ttjejdu778')
    medicamento4 = MedicamentoVL('Ibuebanol', 'Bayer', ean_ok4, '2025-09-23', 'ttjejdu678')
    
    farmacia.agregar_medicamento(medicamento1)
    farmacia.agregar_medicamento(medicamento2)
    farmacia.agregar_medicamento(medicamento3)
    farmacia.agregar_medicamento(medicamento4)

    farmacia.mostrar_medicamentos()
    farmacia.alerta_vencimientos(20)
    farmacia.guardar_csv(f'Inventario {farmacia}.csv')
    
  
  
  
  except (ValidationError, TypeError, ValueError, IndexError) as e:
    print('Error:', e)
  

if __name__ == '__main__':
  main()




















