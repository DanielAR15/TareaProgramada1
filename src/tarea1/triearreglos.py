from tarea1.diccionario import Diccionario

class NodoTrieArreglo:
    """
    Nodo del Trie
    """
    def __init__(self):
        self.simbolos = [""] * 100
        self.hijos = [None] * 100
        self.fin_de_palabra = False


class TrieArreglos(Diccionario):
    """
    Trie con arreglos estáticos , puede contener mayúsculas, minúsculas, tildes, eñes, etc.
    """
    def __init__(self):
        self.raiz = NodoTrieArreglo()
        self.contador = 0

    def _buscar_indice(self, nodo, caracter):
        """
        Busca el índice del carácter en el array del nodo.
        """
        for i in range(len(nodo.simbolos)):
            if nodo.simbolos[i] == caracter:
                return i
        return -1

    def _buscar_posicion_libre(self, nodo):
        """
        Retorna la primera posición libre en el arreglo de símbolos del nodo.
        """
        for i in range(len(nodo.simbolos)):
            if nodo.simbolos[i] == "":
                return i
        return -1

    def inserte(self, hilera):
        """
        Inserta una hilera en el Trie.
        """
        nodo_actual = self.raiz

        for caracter in hilera:
            indice = self._buscar_indice(nodo_actual, caracter)
            if indice == -1:
                pos_libre = self._buscar_posicion_libre(nodo_actual)
                if pos_libre == -1:
                    raise MemoryError("Nodo sin espacio disponible")
                nuevo_nodo = NodoTrieArreglo()
                nodo_actual.simbolos[pos_libre] = caracter
                nodo_actual.hijos[pos_libre] = nuevo_nodo
                nodo_actual = nuevo_nodo
            else:
                nodo_actual = nodo_actual.hijos[indice]

        if not nodo_actual.fin_de_palabra:
            nodo_actual.fin_de_palabra = True
            self.contador += 1

    def miembro(self, hilera):
        """
        Verifica si una hilera existe en el Trie.
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
        self._limpiar_nodos(pila)
        return True

    def _limpiar_nodos(self, pila):
        """
        Limpia nodos vacíos después de borrar una palabra.
        """
        while pila:
            nodo_padre, indice = pila.pop()
            hijo = nodo_padre.hijos[indice]

            if hijo is not None and (hijo.fin_de_palabra or any(hijo.hijos)):
                break

            nodo_padre.simbolos[indice] = ""
            nodo_padre.hijos[indice] = None

            if nodo_padre.fin_de_palabra or any(nodo_padre.hijos):
                break

    def _imprimir_recursivo(self, nodo, prefijo):
        """
        Imprime todas las hileras almacenadas.
        """
        if nodo is None:
            return
        if nodo.fin_de_palabra:
            print(f"  {prefijo}")

        for i in range(len(nodo.simbolos)):
            simbolo = nodo.simbolos[i]
            if simbolo != "" and nodo.hijos[i] is not None:
                self._imprimir_recursivo(nodo.hijos[i], prefijo + simbolo)

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
        if nodo is None:
            return
        if nodo.fin_de_palabra:
            elementos.append(prefijo)

        for i in range(len(nodo.simbolos)):
            simbolo = nodo.simbolos[i]
            if simbolo != "" and nodo.hijos[i] is not None:
                self.juntar_elementos(nodo.hijos[i], prefijo + simbolo, elementos)

    def limpie(self):
        """
        Elimina todo el contenido del Trie.
        """
        self.raiz = NodoTrieArreglo()
        self.contador = 0

    def __str__(self):
        """
        Devuelve una representación textual del Trie.
        """
        elementos = []
        self.juntar_elementos(self.raiz, "", elementos)
        return f"TrieArreglos({', '.join(sorted(elementos))})"

    def __len__(self):
        """
        Devuelve la cantidad de elementos en el Trie.
        """
        return self.contador
