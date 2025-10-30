import numpy as np
import matplotlib.pyplot as plt

# Matrices separadas: unidades vendidas
unidades = np.array([
[1250, 1380, 1420, 1650], # Alpha
[980, 1050, 1020, 1150], # Beta
[1560, 1680, 1590, 1820], # Gamma
[870, 920, 890, 1010], # Delta
[1340, 1450, 1480, 1620], # Epsilon
[760, 810, 780, 890] # Zeta
])


# Ingresos ($)
ingresos = np.array([
[56250, 62100, 63900, 74250],
[58800, 63000, 61200, 69000],
[54600, 58800, 55650, 63700],
[60900, 64400, 62300, 70700],
[60300, 65250, 66600, 72900],
[49400, 52650, 50700, 57850]
])


productos = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta']
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']


# NIVEL 1: METRICAS DE DESEMPENIO 

# 1) Ventas totales anuales por producto
unidades_totales_anuales = np.sum(unidades, axis=1)   # suma de Q1..Q4 por producto
ingresos_totales_anuales = np.sum(ingresos, axis=1)   # suma de Q1..Q4 por producto

print("Totales anuales por producto:")
for i, prod in enumerate(productos):
    print(f"{prod:<8} Unidades: {unidades_totales_anuales[i]:}  |  Ingresos: ${ingresos_totales_anuales[i]:.0f}")


# 2) Precio promedio por trimestre (ingresos / unidades), por producto
precio_unitario = ingresos / unidades      # matriz 6x4: precio por producto y trimestre
print("\nPrecio promedio por unidad (por trimestre):")
for i, prod in enumerate(productos):
    q_str = "  ".join([f"{trimestres[j]}=${precio_unitario[i, j]:.2f}" for j in range(4)])
    print(f"{prod:<8} {q_str}")


# promedio anual de precio por producto
precio_prom_anual = np.mean(precio_unitario, axis=1)


# 3) Producto con mayores ingresos en el año
idx_max = np.argmax(ingresos_totales_anuales)
print(f"\nMayor ingreso anual: {productos[idx_max]} con ${ingresos_totales_anuales[idx_max]:.0f}")



# 4) Ingresos totales por trimestre (suma de todos los productos)
ingresos_totales_trimestre = np.sum(ingresos, axis=0)  # suma por columnas Q1..Q4
print("\nIngresos totales por trimestre:")
for j, tri in enumerate(trimestres):
    print(f"{tri}: ${ingresos_totales_trimestre[j]:.0f}")





# NIVEL 2: ANALISIS DE CRECIMIENTO 


# 5) Crecimiento porcentual de UNIDADES (promedio de diferencias / promedio anual)
dif_trimestres_u = np.diff(unidades, axis=1)            # Q2-Q1, Q3-Q2, Q4-Q3
prom_dif_u = dif_trimestres_u.mean(axis=1)              # promedio de esas diferencias
base_u = unidades.mean(axis=1)                          # promedio de todas las unidades del año
crec_unidades_pct = (prom_dif_u / base_u) * 100         # % de crecimiento promedio

print("\nCrecimiento porcentual promedio TRIMESTRAL en UNIDADES (base promedio anual) =")
for i, prod in enumerate(productos):
    print(f"{prod:<8}: {crec_unidades_pct[i]:.2f}% por trimestre")

# 6) Crecimiento porcentual de INGRESOS (mismo método)
dif_trimestres_ing = np.diff(ingresos, axis=1)
prom_dif_ing = dif_trimestres_ing.mean(axis=1)
base_ing = ingresos.mean(axis=1)
crec_ingresos_pct = (prom_dif_ing / base_ing) * 100

print("\nCrecimiento porcentual promedio TRIMESTRAL en INGRESOS (base promedio anual) =")
for i, prod in enumerate(productos):
    print(f"{prod:<8}: {crec_ingresos_pct[i]:.2f}% por trimestre")

# 7) Producto con mayor crecimiento (en unidades)
idx_crec = np.argmax(crec_unidades_pct)
print(f"\n Mayor crecimiento (unidades) ===\n{productos[idx_crec]} con {crec_unidades_pct[idx_crec]:.2f}% por trimestre")

# 8) Productos con crecimiento NEGATIVO (usando máscara NumPy)
mask_neg = crec_unidades_pct < 0
if np.any(mask_neg):
    print("\nProductos con crecimiento NEGATIVO (unidades)")
    for prod, val in zip(np.array(productos)[mask_neg], crec_unidades_pct[mask_neg]):
        print(f"{prod}: {val:.2f}% por trimestre")
else:
    print("\nNo hubo crecimiento negativo en unidades")

# 9) La tasa de crecimiento promedio trimestral ya está representada en 'crec_unidades_pct' y 'crec_ingresos_pct'.


# NIVEL 3: Análisis de Rentabilidad


# 10) Ingreso promedio por unidad (promedio de los 4 trimestres)
ingreso_promedio_unidad = np.mean(precio_unitario, axis=1)

# 11) Producto más "premium"
idx_premium = np.argmax(ingreso_promedio_unidad)

# 12) Porcentaje de los ingresos totales que representa cada producto
porcentaje_ingresos = (ingresos_totales_anuales / np.sum(ingresos_totales_anuales)) * 100


# 13) Mejor trimestre de cada producto
mejor_trim = np.argmax(ingresos, axis=1)

print("\n=== NIVEL 3: Análisis de Rentabilidad ===")
for i, prod in enumerate(productos):
    print(f"{prod:<8} Promedio $/u: ${ingreso_promedio_unidad[i]:.2f}  |  %Total: {porcentaje_ingresos[i]:.2f}%  |  Mejor trimestre: {trimestres[mejor_trim[i]]}")

print(f"\nProducto más premium: {productos[idx_premium]} (${ingreso_promedio_unidad[idx_premium]:.2f} por unidad)")


# NIVEL 4: Proyecciones y Visualización


# 14) Proyección lineal simple para Q1-2024 (usando tendencia lineal)
# y = m*x + b   → usamos np.polyfit
proyecciones = []
for i in range(len(productos)):
    coef = np.polyfit([1, 2, 3, 4], ingresos[i], 1)
    proyeccion = np.polyval(coef, 5)  # trimestre 5 = Q1 2024
    proyecciones.append(proyeccion)

print("\nProyección de ingresos para Q1 2024 ===")
for i, prod in enumerate(productos):
    print(f"{prod:<8}: ${proyecciones[i]:,.0f}")

# 15) Clasificación de productos estrella / problema
prom_ingresos = np.mean(ingresos_totales_anuales)
prom_crec = np.mean(crec_unidades_pct)

productos_estrella = [productos[i] for i in range(len(productos)) if ingresos_totales_anuales[i] > prom_ingresos and crec_unidades_pct[i] > prom_crec]
productos_problema = [productos[i] for i in range(len(productos)) if ingresos_totales_anuales[i] < prom_ingresos and crec_unidades_pct[i] < prom_crec]

print("\n=== 15) Clasificación ===")
print("Productos estrella:", productos_estrella)
print("Productos problema:", productos_problema)


# 16) GRÁFICOS 
# --- Gráfico 1: Evolución de ingresos por producto ---
plt.figure(figsize=(12, 6))
for i in range(len(productos)):
    plt.plot(trimestres, ingresos[i], marker='o', label=productos[i])
plt.title("Evolución de Ingresos por Producto (2023)")
plt.xlabel("Trimestre")
plt.ylabel("Ingresos ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Gráfico 2: Crecimiento promedio trimestral en UNIDADES (en %) ---

plt.figure(figsize=(10, 5))
plt.bar(productos, crec_unidades_pct)
plt.axhline(0, linewidth=0.8)
plt.title("Crecimiento porcentual promedio trimestral en unidades")
plt.ylabel("Crecimiento promedio por trimestre (%)")
plt.tight_layout()
plt.show()
