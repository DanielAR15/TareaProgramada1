from tarea1.listaordenadadinamica import ListaOrdenadaDinámica
from tarea1.listaordenadaestatica import ListaOrdenadaEstática
from tarea1.tablahashabierta import TablaHashAbierta
from tarea1.triepunteros import TriePunteros
from tarea1.triearreglos import TrieArreglos


def probar_diccionario(diccionario, nombre="Diccionario"):
    print(f"\nProbando {nombre}...")

    #al estar vacía no pueden estar sin ser insertadas antes
    diccionario.limpie()
    assert diccionario.miembro("habitación") is False
    assert diccionario.miembro("azul") is False

    # Insertar elementos a la estructura de datos
    diccionario.inserte("programa de televisión")
    diccionario.inserte("hola")
    diccionario.inserte("bola")
    diccionario.inserte("mariposa")

    assert diccionario.miembro("programa de televisión") is True
    assert diccionario.miembro("hola") is True
    assert diccionario.miembro("bola") is True
    assert diccionario.miembro("zzz") is False

    # Eliminar elementos de la estructura
    diccionario.borre("bola")
    diccionario.borre("mariposa")

    assert diccionario.miembro("bola") is False
    assert diccionario.miembro("mariposa") is False

    # Eliminar un elemento inexistente (deberia de seguir funcionando aunque no exista)
    diccionario.borre("caballo")

    # Insertar duplicados
    diccionario.inserte("cocina")
    diccionario.inserte("cocina")
    assert diccionario.miembro("cocina") is True  # sigue estando

    # Imprimir la estructura de datos
    print("Contenido actual de la estructura de datos:")
    diccionario.imprima()

    # Limpiar
    diccionario.limpie()
    assert len(diccionario) == 0

    #imprimir luego de limpiar para verificar
    print("Contenido actual de la estructura de datos:")
    diccionario.imprima()

    print(f"{nombre} completó las pruebas.")

if __name__ == "__main__":
    # Prueba con lista enlazada dinámica
    probar_diccionario(ListaOrdenadaDinámica(), "ListaOrdenadaDinámica")

    # Prueba con lista estática de tamaño fijo
    probar_diccionario(ListaOrdenadaEstática(100), "ListaOrdenadaEstática")

    #Prueba con la tabla hash 
    probar_diccionario(TablaHashAbierta(10), "TablaHashAbierta")

    #Prueba con el trie de punteros
    probar_diccionario(TriePunteros(), "Trie punteros")

    #Prueba con el trie de arreglos
    probar_diccionario(TrieArreglos(), "Trie arreglos")

    print("\nSe terminó la implementación y depuración :)")
