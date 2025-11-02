# Diccionario y Estructuras de Datos en Python

## Descripción
Este proyecto implementa diversas estructuras de datos de tipo diccionario en Python, incluyendo:

- Lista Ordenada Dinámica
- Lista Ordenada Estática
- Tabla Hash Abierta
- Árbol Binario de Búsqueda (ABB) con punteros y con vector heap
- Trie con punteros y con arreglos

El programa permite al usuario interactuar mediante menús en consola para **insertar, borrar, buscar, imprimir y limpiar elementos** en las estructuras. También se contemplan pruebas de rendimiento (benchmarking), aunque no todas están implementadas aún.

---

## Requisitos

- Python 3.10 o superior
- Biblioteca [Rich](https://pypi.org/project/rich/) para visualización en consola

---
## Instalación de dependencias

pip install rich

---

## Estructura del proyecto

<img width="569" height="312" alt="{558185AB-0D7B-495D-98DD-76D558564E11}" src="https://github.com/user-attachments/assets/ba1215e5-85d5-44b1-9a14-b20aabe79e27" />

    
---
## ejecucion del programa

python -m tarea1

## ejecucion de las pruebas

Primero navegas al directorio src y colocas :
>$env:PYTHONPATH = "src"

Luego te diriges a la carpeta base, con el comando --> cd ..
 Si quieres ejecutar las pruebas generales de las tres estructuras coloca este comando:
>python test/main_test.py 

Si quieres probar la aleatoriedad y redistribución de la has coloca:

>python test_aleatoriedadhash.py

Si vas a ejecutar las pruebas de rendimiento, debes colocar:
>python -m tarea1.pruebas_de_rendimiento

Luego, para ejecutar el file que crea los gráficos, colocas:
>python test/analisis_datos.py
---
## Menu Principal

- Menú principal

    1. Menú de diccionarios: elegir la estructura de datos.
    2. Pruebas de rendimiento: benchmarking de inserción, búsqueda y borrado (pendiente de implementación).

- Menú de operaciones de diccionario

    - Agregar un elemento
    - Borrar un elemento
    - Verificar existencia
    - Imprimir el diccionario
    - Limpiar el diccionario
    - Salir
