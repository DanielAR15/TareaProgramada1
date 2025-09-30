from tarea1.listaordenadadinamica import ListaOrdenadaDinámica

def main():
    dic = ListaOrdenadaDinámica()

    while True:
        print("\n=== Menú Diccionario (Lista Ordenada Dinámica) ===")
        print("1. Insertar")
        print("2. Borrar")
        print("3. Miembro")
        print("4. Imprimir")
        print("5. Limpiar")
        print("6. Tamaño")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            e = input("Elemento a insertar: ")
            dic.inserte(e)
            print(f"'{e}' insertado correctamente.")

        elif opcion == "2":
            e = input("Elemento a borrar: ")
            dic.borre(e)
            print(f"'{e}' borrado si existía.")

        elif opcion == "3":
            e = input("Elemento a buscar: ")
            print("Sí está en el diccionario." if dic.miembro(e) else "No está en el diccionario.")

        elif opcion == "4":
            print("Contenido del diccionario:")
            dic.imprima()

        elif opcion == "5":
            dic.limpie()
            print("Diccionario limpiado.")

        elif opcion == "6":
            print(f"El diccionario tiene {len(dic)} elementos.")

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
