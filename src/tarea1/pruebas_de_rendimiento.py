# -*- coding: utf-8 -*-
"""
Pruebas de rendimiento para las estructuras de datos del Modelo Diccionario.
mide inserte, miembro, borre, print, done y memoria.
"""
import time
import random
import string
import csv
import tracemalloc
from pathlib import Path

SIZES = [100, 1000]   
NUM_RUNS = 10
OUTPUT_CSV = "resultados_rendimiento.csv"
MEASURE_MEMORY = True
STRING_LENGTH = 20

DATA_MODE = "random"

from tarea1.listaordenadadinamica import ListaOrdenadaDinámica
from tarea1.listaordenadaestatica import ListaOrdenadaEstática
from tarea1.tablahashabierta import TablaHashAbierta
from tarea1.tablahash import TablaHash
from tarea1.triepunteros import TriePunteros
from tarea1.triearreglos import TrieArreglos
from tarea1.abbpunteros import AbbPunteros
from tarea1.abbvectorheap import ABBVectorHeap

comparaciones = [
    ("ListaOrdenadaDinámica", lambda: ListaOrdenadaDinámica(), "ListaOrdenadaEstática", lambda: ListaOrdenadaEstática(2000)),
    ("AbbPunteros", lambda: AbbPunteros(), "ABBVectorHeap", lambda: ABBVectorHeap(6000)),
    ("TriePunteros", lambda: TriePunteros(), "TrieArreglos", lambda: TrieArreglos()),
    ("ListaOrdenadaDinámica", lambda: ListaOrdenadaDinámica(), "TablaHash", lambda: TablaHash()),
    ("ListaOrdenadaDinámica", lambda: ListaOrdenadaDinámica(), "AbbPunteros", lambda: AbbPunteros()),
    ("ListaOrdenadaDinámica", lambda: ListaOrdenadaDinámica(), "TriePunteros", lambda: TriePunteros()),
    ("TablaHash", lambda: TablaHash(), "TriePunteros", lambda: TriePunteros())
]

def generar_cadenas(n, largo=STRING_LENGTH, modo="random"):
    abc = string.ascii_lowercase
    if modo == "random":
        return [''.join(random.choices(abc, k=largo)) for _ in range(n)]
    elif modo == "shared_prefix":
        prefix = ''.join(random.choices(abc, k=max(1, largo // 2)))
        return [prefix + ''.join(random.choices(abc, k=largo - len(prefix))) for _ in range(n)]
    elif modo == "distinct_prefix":
        res = []
        for _ in range(n):
            pre = ''.join(random.choices(abc, k=6))
            suf = ''.join(random.choices(abc, k=max(0, largo - 6)))
            res.append(pre + suf)
        return res
    else:
        raise ValueError("Modo de datos desconocido")

def medir_estructura(estructura, datos):
    if MEASURE_MEMORY:
        tracemalloc.start()
    t0 = time.perf_counter()
    for h in datos:
        estructura.inserte(h)
    t1 = time.perf_counter()
    insertar_ms = (t1 - t0) * 1000.0

    memoria_kb = 0.0
    if MEASURE_MEMORY:
        current, peak = tracemalloc.get_traced_memory()
        memoria_kb = peak / 1024.0
        tracemalloc.stop()

    # Medir miembro (búsqueda)
    t0 = time.perf_counter()
    for h in datos[:len(datos)//2]:
        estructura.miembro(h)
    t1 = time.perf_counter()
    miembro_ms = (t1 - t0) * 1000.0

    # Medir borrado
    t0 = time.perf_counter()
    for h in datos[:len(datos)//4]:
        try:
            estructura.borre(h)
        except Exception:
            pass
    t1 = time.perf_counter()
    borrar_ms = (t1 - t0) * 1000.0

    return insertar_ms, miembro_ms, borrar_ms, memoria_kb

def medir_print_done(estructura):
    try:
        t0 = time.perf_counter()
        estructura.print()
        t1 = time.perf_counter()
        print_ms = (t1 - t0) * 1000.0
    except Exception:
        print_ms = float("nan")

    try:
        t0 = time.perf_counter()
        estructura.done()
        t1 = time.perf_counter()
        done_ms = (t1 - t0) * 1000.0
    except Exception:
        done_ms = float("nan")

    return print_ms, done_ms

"""
Escribe el .csv y le da el formato
"""
def preparar_csv(path: str):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([
            "comparacion", "estructura", "tamano", "ejecucion",
            "inserte_ms", "miembro_ms", "borre_ms",
            "print_ms", "done_ms", "memoria_pico_kb"
        ])


def pruebas_de_rendimiento():
    preparar_csv(OUTPUT_CSV)

    with open(OUTPUT_CSV, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        for (nombre1, clase1, nombre2, clase2) in comparaciones:
            print(f"\n=== Comparación: {nombre1} vs {nombre2} ===")
            for tamano in SIZES:
                print(f"  - Tamaño: {tamano}")
                for run in range(1, NUM_RUNS + 1):
                    print(f"    • Ejecución {run}/{NUM_RUNS} ...", end="", flush=True)
                    datos = generar_cadenas(tamano, STRING_LENGTH, modo=DATA_MODE)

                    e1 = clase1()
                    e2 = clase2()

                    # Estructura 1
                    try:
                        ins1, mem1, del1, mem_kb1 = medir_estructura(e1, datos)
                        print_ms1, done_ms1 = (medir_print_done(e1) if tamano == 1_000_000 else (0.0, 0.0))
                    except Exception as ex:
                        print(f"\nError en {nombre1}: {ex}")
                        ins1 = mem1 = del1 = mem_kb1 = print_ms1 = done_ms1 = float("nan")

                    # Estructura 2
                    try:
                        ins2, mem2, del2, mem_kb2 = medir_estructura(e2, datos)
                        print_ms2, done_ms2 = (medir_print_done(e2) if tamano == 1_000_000 else (0.0, 0.0))
                    except Exception as ex:
                        print(f"\nError en {nombre2}: {ex}")
                        ins2 = mem2 = del2 = mem_kb2 = print_ms2 = done_ms2 = float("nan")

                    writer.writerow([
                        f"{nombre1} vs {nombre2}", nombre1, tamano, run,
                        f"{ins1:.3f}", f"{mem1:.3f}", f"{del1:.3f}",
                        f"{print_ms1:.3f}", f"{done_ms1:.3f}", f"{mem_kb1:.3f}"
                    ])
                    writer.writerow([
                        f"{nombre1} vs {nombre2}", nombre2, tamano, run,
                        f"{ins2:.3f}", f"{mem2:.3f}", f"{del2:.3f}",
                        f"{print_ms2:.3f}", f"{done_ms2:.3f}", f"{mem_kb2:.3f}"
                    ])
                    print(" hecho")

    print(f"\nPruebas completadas. Resultados guardados en {OUTPUT_CSV}")


if __name__ == "__main__":
    pruebas_de_rendimiento()
