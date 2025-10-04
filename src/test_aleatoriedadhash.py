import statistics
from tarea1.tablahashabierta import TablaHashAbierta

def evaluar_distribucion():
    capacidad = 50
    tabla = TablaHashAbierta(capacidad=capacidad)

    elementos = [f"cadena{i}" for i in range(1000)]
    for e in elementos:
        tabla.inserte(e)

    distribucion = [len(bucket) for bucket in tabla.tabla]

    promedio = statistics.mean(distribucion)
    desviacion = statistics.pstdev(distribucion)

    print("\n--- Evaluación de aleatoriedad ---")
    print(f"Capacidad de la tabla: {capacidad}")
    print(f"Número de elementos: {len(elementos)}")
    print(f"Promedio esperado por cubeta: {promedio:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")

    if desviacion < promedio * 2:
        print("Distribución uniforme")
    else:
        print("Alta concentración")

if __name__ == "__main__":
    evaluar_distribucion()
