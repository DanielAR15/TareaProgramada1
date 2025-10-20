from tarea1.diccionario import Diccionario

class NodoTrieArreglo:
    """
    Nodo para el Trie usando arreglos.
    """
    def __init__(self):
        self.simbolos = []
        self.hijos = []
        self.fin_de_palabra = False


class TrieArreglos(Diccionario):
    """
    Trie implementado con arreglos
    """
    def __init__(self):
        self.raiz = NodoTrieArreglo()
        self.contador = 0

    def _buscar_indice(self, nodo, caracter):
        """
        Busca el índice de un carácter en la lista de símbolos del nodo.
        """
        for i in range(len(nodo.simbolos)):
            if nodo.simbolos[i] == caracter:
                return i
        return -1

    def inserte(self, hilera):
        """
        Inserta una hilera (cadena) en el Trie.
        """
        nodo_actual = self.raiz

        for caracter in hilera:
            indice = self._buscar_indice(nodo_actual, caracter)
            if indice == -1:
                nuevo_nodo = NodoTrieArreglo()
                nodo_actual.simbolos.append(caracter)
                nodo_actual.hijos.append(nuevo_nodo)
                nodo_actual = nuevo_nodo
            else:
                nodo_actual = nodo_actual.hijos[indice]

        if not nodo_actual.fin_de_palabra:
            nodo_actual.fin_de_palabra = True
            self.contador += 1

    def miembro(self, hilera):
        """
        Verifica si la hilera ingresada como parámetro existe en el Trie.
        """
        nodo_actual = self.raiz

        for caracter in hilera:
            indice = self._buscar_indice(nodo_actual, caracter)
            if indice == -1:
                return False
            nodo_actual = nodo_actual.hijos[indice]

        return nodo_actual.fin_de_palabra

    def borre(self, hilera):
        """
        Elimina una hilera del Trie si existe.
        """
        pila = []
        nodo_actual = self.raiz

        for caracter in hilera:
            indice = self._buscar_indice(nodo_actual, caracter)
            if indice == -1:
                return False
            pila.append((nodo_actual, indice))
            nodo_actual = nodo_actual.hijos[indice]

        if not nodo_actual.fin_de_palabra:
            return False

        nodo_actual.fin_de_palabra = False
        self.contador -= 1
        self._limpiar_nodos(pila, nodo_actual)
        return True

    def _limpiar_nodos(self, pila, nodo_actual):
        """
        Limpia los nodos que quedan sin uso después de borrar una palabra.
        """
        if nodo_actual.fin_de_palabra or nodo_actual.hijos:
            return

        while pila:
            nodo_padre, indice = pila.pop()
            del nodo_padre.simbolos[indice]
            del nodo_padre.hijos[indice]
            if nodo_padre.fin_de_palabra or nodo_padre.hijos:
                break

    def _imprimir_recursivo(self, nodo, prefijo):
        """
        Función para imprimir todas las hileras almacenadas.
        """
        if nodo.fin_de_palabra:
            print(f"  {prefijo}")

        pares = sorted(zip(nodo.simbolos, nodo.hijos), key=lambda x: x[0])
        for caracter, hijo in pares:
            self._imprimir_recursivo(hijo, prefijo + caracter)

    def imprima(self):
        """
        Imprime todas las hileras almacenadas en el Trie.
        """
        if self.contador == 0:
            print("El Trie está vacío")
            return

        print(f"Tiene {self.contador} elementos:")
        self._imprimir_recursivo(self.raiz, "")

    def juntar_elementos(self, nodo, prefijo, elementos):
        """
        Junta todos los elementos del Trie en una lista.
        """
        if nodo.fin_de_palabra:
            elementos.append(prefijo)

        for i in range(len(nodo.simbolos)):
            self.juntar_elementos(nodo.hijos[i], prefijo + nodo.simbolos[i], elementos)

    def limpie(self):
        """
        Elimina todo el contenido del Trie.
        """
        self.raiz = NodoTrieArreglo()
        self.contador = 0

    def __str__(self):
        """
        Devuelve una representación de texto del Trie.
        """
        elementos = []
        self.juntar_elementos(self.raiz, "", elementos)
        return f"TrieArreglos({', '.join(sorted(elementos))})"

    def __len__(self):
        """
        Devuelve el número de elementos en el Trie.
        """
        return self.contador
