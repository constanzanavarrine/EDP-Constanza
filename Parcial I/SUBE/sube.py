# main.py
import csv
from validador_entrada import ValidadorEntrada
from analizadorsube import AnalizadorSube

def leer_csv_como_dicts(path: str):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def pedir_con_reintento(mensaje, validador):
    while True:
        try:
            valor_bruto = input(mensaje)
            valor_limpio = validador(valor_bruto)
            return valor_limpio
        except ValueError as e:
            print(f"✗ {e} — probá otra vez.")

def main():
    datos = leer_csv_como_dicts("total-usuarios-por-dia.csv")
    analizador = AnalizadorSube(datos)

    print("Años disponibles:", sorted(analizador.anios_disponibles))
    print("Transportes:", sorted(analizador.transportes_disponibles))

    # 1) Validar año contra los disponibles del dataset
    validar_anio = lambda s: ValidadorEntrada.anio(s, analizador.anios_disponibles) # porque analizador es analizadorsube y anios_disponibles quedaron almacenados en un self por eso puedo acceder a estos 
    anio = pedir_con_reintento("Ingresá año (p.ej. 2020): ", validar_anio)

    # 2) Validar mes 1..12
    mes = pedir_con_reintento("Ingresá mes (1..12): ", ValidadorEntrada.mes)

    # 3) (Opcional) Validar transporte por si querés pedirlo en otra tarea
    # validar_transporte = lambda s: ValidadorEntrada.transporte(s, analizador.transportes_disponibles)
    # transporte = pedir_con_reintento("Medio: ", validar_transporte)

    # Ejecutar análisis: medio más usado en ese mes/año
    medio, usuarios = analizador.medio_mas_usado_mes(anio, mes)
    print(f"En {anio}-{mes:02d}, el medio más usado fue '{medio}' con {usuarios:,} usuarios.")

if __name__ == "__main__":
    main()



        
        


