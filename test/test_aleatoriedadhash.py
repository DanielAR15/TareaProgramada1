import statistics
import time
import random
import string
from tarea1.tablahashabierta import TablaHashAbierta

def generar_string(longitud=12):
    """
    Genera una cadena aleatoria de letras minúsculas.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(longitud))

def evaluar_distribucion():
    capacidad = 50
    tabla = TablaHashAbierta(capacidad=capacidad)

    elementos = [f"cadena{i}" for i in range(1000)]
    for e in elementos:
        tabla.inserte(e)

    distribucion = [len(bucket) for bucket in tabla.tabla]

    promedio = statistics.mean(distribucion)
    desviacion = statistics.pstdev(distribucion)
    minimo = min(distribucion)
    maximo = max(distribucion)

    print("\n--- Evaluación de aleatoriedad ---")
    print(f"Capacidad de la tabla: {capacidad}")
    print(f"Número de elementos: {len(elementos)}")
    print(f"Promedio esperado por cubeta: {promedio:.2f}")
    print(f"Mínimo: {minimo}, Máximo: {maximo}")
    print(f"Desviación estándar: {desviacion:.2f}")

    if desviacion < promedio * 2:
        print("Distribución uniforme")
    else:
        print("Alta concentración")

def evaluar_redistribucion():
    """
    Se evalua el tiempo que tarda el proceso de rehash.
    """
    print("\n- Evaluación del proceso de redistribución -")

    tabla = TablaHashAbierta(capacidad=8)
    elementos = [generar_string() for _ in range(20000)]

    inicio = time.perf_counter()
    for e in elementos:
        tabla.inserte(e)
    fin = time.perf_counter()

    duracion = fin - inicio

    print(f"Tiempo total de inserciones: {duracion:.4f} seg")
    print(f"Capacidad final de la tabla: {tabla.capacidad}")
    print(f"Elementos almacenados: {len(elementos)}")
    if hasattr(tabla, 'rehashes'):
        print(f"Rehash realizados: {tabla.rehashes}")


if __name__ == "__main__":
    evaluar_distribucion()
    evaluar_redistribucion()