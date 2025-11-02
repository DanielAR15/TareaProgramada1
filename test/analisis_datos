# -*- coding: utf-8 -*-
"""
Analiza los resultados de rendimiento y memoria de las estructuras de datos
a partir del archivo CSV generado por pruebas_de_rendimiento.py.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

INPUT_CSV = "resultados_rendimiento.csv"
OUTPUT_DIR = Path("analisis_resultados")
OUTPUT_DIR.mkdir(exist_ok=True)

print("📂 Leyendo los datos de:", INPUT_CSV)
df = pd.read_csv(INPUT_CSV, encoding="utf-8")

# --- Normalizar nombres de columnas ---
df.columns = [c.strip().lower().replace("ó", "o").replace("í", "i").replace("é", "e").replace("á", "a").replace("ú", "u") for c in df.columns]

# Convertir columnas numéricas
columnas_numericas = ["inserte_ms", "miembro_ms", "borre_ms", "memoria_pico_kb"]
for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Limpiar filas con datos faltantes
filas_antes = len(df)
df = df.dropna(subset=columnas_numericas)
print(f"📉 Filas eliminadas por datos incompletos: {filas_antes - len(df)}")

# ---------- ESTADÍSTICAS ----------
print("\n📈 Calculando promedios y desviaciones estándar...")

agrupado = df.groupby(["comparacion", "estructura", "tamano"]).agg(
    inserte_promedio=("inserte_ms", "mean"),
    miembro_promedio=("miembro_ms", "mean"),
    borre_promedio=("borre_ms", "mean"),
    memoria_promedio=("memoria_pico_kb", "mean"),
).reset_index()

csv_out = OUTPUT_DIR / "resultados_rendimiento_agrupado.csv"
agrupado.to_csv(csv_out, index=False)
print(f"✅ Resultados estadísticos guardados en {csv_out}")

# ---------- FUNCIONES DE GRAFICADO ----------
def graficar_comparacion(df_comp, comparacion):
    """Crea dos gráficos por comparación: tiempos y memoria"""
    estructuras = df_comp["estructura"].unique()

    # --- Gráfico de tiempos ---
    plt.figure(figsize=(8, 5))
    plt.title(f"Tiempos Promedio\nComparación: {comparacion}")
    for estructura in estructuras:
        sub = df_comp[df_comp["estructura"] == estructura].sort_values(by="tamano")  # 🔹 ordena por tamaño
        plt.plot(sub["tamano"], sub["inserte_promedio"], marker="o", label=f"{estructura} - inserte")
        plt.plot(sub["tamano"], sub["miembro_promedio"], marker="s", label=f"{estructura} - miembro")
        plt.plot(sub["tamano"], sub["borre_promedio"], marker="^", label=f"{estructura} - borre")
    plt.xlabel("Tamaño del diccionario (N)")
    plt.ylabel("Tiempo (ms)")
    plt.xscale("log")
    plt.legend(title="Estructura y operación", fontsize=8)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"{comparacion.replace(' ', '_')}_tiempos.png")
    plt.close()

    # --- Gráfico de memoria ---
    plt.figure(figsize=(8, 5))
    plt.title(f"Uso de Memoria Promedio\nComparación: {comparacion}")
    for estructura in estructuras:
        sub = df_comp[df_comp["estructura"] == estructura].sort_values(by="tamano")  # 🔹 ordena por tamaño
        plt.plot(sub["tamano"], sub["memoria_promedio"], marker="o", label=estructura)
    plt.xlabel("Tamaño del diccionario (N)")
    plt.ylabel("Memoria pico (KB)")
    plt.xscale("log")
    plt.legend(title="Estructura", fontsize=8)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"{comparacion.replace(' ', '_')}_memoria.png")
    plt.close()

    print(f"📊 Gráficos guardados para {comparacion}")

def graficar_general(df):
    """Gráfico global con todas las comparaciones y estructuras"""
    plt.figure(figsize=(9, 6))
    plt.title("Resumen General: Tiempos Promedio de Inserción")
    for estructura in df["estructura"].unique():
        sub = df[df["estructura"] == estructura].sort_values(by="tamano")  # 🔹 ordena por tamaño
        plt.plot(sub["tamano"], sub["inserte_promedio"], marker="o", label=estructura)
    plt.xlabel("Tamaño del diccionario (N)")
    plt.ylabel("Tiempo de inserción promedio (ms)")
    plt.xscale("log")
    plt.legend(title="Estructura", fontsize=9)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "general_tiempos.png")
    plt.close()

    plt.figure(figsize=(9, 6))
    plt.title("Resumen General: Uso de Memoria Promedio")
    for estructura in df["estructura"].unique():
        sub = df[df["estructura"] == estructura].sort_values(by="tamano")  # 🔹 ordena por tamaño
        plt.plot(sub["tamano"], sub["memoria_promedio"], marker="s", label=estructura)
    plt.xlabel("Tamaño del diccionario (N)")
    plt.ylabel("Memoria pico (KB)")
    plt.xscale("log")
    plt.legend(title="Estructura", fontsize=9)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "general_memoria.png")
    plt.close()

    print("📊 Gráficos generales guardados.")

# ---------- GRAFICAR ----------
print("\n🎨 Generando gráficos de las comparaciones...")

for comp in agrupado["comparacion"].unique():
    df_comp = agrupado[agrupado["comparacion"] == comp]
    graficar_comparacion(df_comp, comp)

print("\n🎨 Generando gráficos generales...")
graficar_general(agrupado)

print("\nResumen de análisis (primeras filas):")
print(agrupado.head(10).to_string(index=False))
print("\n✅ Análisis completado. Gráficos guardados en 'analisis_resultados'.")
