from tarea1.diccionario import Diccionario

class NodoABB:
    """Nodo de un Árbol Binario de Búsqueda (ABB)."""
    def __init__(self, elemento: str):
        self.elemento = elemento
        self.izquierdo: NodoABB | None = None
        self.derecho: NodoABB | None = None


class AbbPunteros(Diccionario):
    """
    Implementación del Diccionario usando un Árbol Binario de Búsqueda (ABB) por punteros.
    """

    def __init__(self):
        """Inicializa un árbol vacío."""
        self.raiz: NodoABB | None = None
        self._tamaño = 0


    # métodos  ---------------------------

    def _insertar_rec(self, nodo: NodoABB | None, elemento: str) -> NodoABB:
        """
        Inserta recursivamente un elemento manteniendo la propiedad del ABB.
        """
        if nodo is None:
            self._tamaño += 1
            return NodoABB(elemento)
        if elemento < nodo.elemento:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, elemento)
        elif elemento > nodo.elemento:
            nodo.derecho = self._insertar_rec(nodo.derecho, elemento)
        # Si es igual, no se inserta duplicado (opcional)
        return nodo

    def _buscar_rec(self, nodo: NodoABB | None, elemento: str) -> bool:
        """
        Busca recursivamente un elemento en el árbol.
        """
        if nodo is None:
            return False
        if elemento == nodo.elemento:
            return True
        elif elemento < nodo.elemento:
            return self._buscar_rec(nodo.izquierdo, elemento)
        else:
            return self._buscar_rec(nodo.derecho, elemento)

    def _minimo(self, nodo: NodoABB) -> NodoABB:
        """
        Devuelve el nodo con el valor mínimo (más a la izquierda).
        """
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

    def _borrar_rec(self, nodo: NodoABB | None, elemento: str) -> NodoABB | None:
        """
        Elimina recursivamente un elemento del árbol.
        """
        if nodo is None:
            return None

        if elemento < nodo.elemento:
            nodo.izquierdo = self._borrar_rec(nodo.izquierdo, elemento)
        elif elemento > nodo.elemento:
            nodo.derecho = self._borrar_rec(nodo.derecho, elemento)
        else:
            # Caso 1: sin hijos
            if nodo.izquierdo is None and nodo.derecho is None:
                self._tamaño -= 1
                return None
            # Caso 2: un solo hijo
            elif nodo.izquierdo is None:
                self._tamaño -= 1
                return nodo.derecho
            elif nodo.derecho is None:
                self._tamaño -= 1
                return nodo.izquierdo
            # Caso 3: dos hijos
            sucesor = self._minimo(nodo.derecho)
            nodo.elemento = sucesor.elemento
            nodo.derecho = self._borrar_rec(nodo.derecho, sucesor.elemento)
        return nodo

    def _inorden(self, nodo: NodoABB | None, resultado: list[str]):
        """Recorrido inorden para obtener los elementos ordenados."""
        if nodo:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.elemento)
            self._inorden(nodo.derecho, resultado)

    # Metodoos del diccionario ---------------------------

    def inserte(self, elemento: str):
        """
        Inserta un nuevo elemento en el ABB.
        """
        self.raiz = self._insertar_rec(self.raiz, elemento)

    def borre(self, elemento: str) -> bool:
        """
        Elimina un elemento del ABB si existe.
        """
        if not self.miembro(elemento):
            return False
        self.raiz = self._borrar_rec(self.raiz, elemento)
        return True

    def miembro(self, elemento: str) -> bool:
        """
        Verifica si un elemento existe en el ABB.
        """
        return self._buscar_rec(self.raiz, elemento)

    def limpie(self):
        """
        Elimina todos los elementos del árbol.
        """
        self.raiz = None
        self._tamaño = 0

    def imprima(self):
        """
        Imprime los elementos en orden ascendente.
        """
        elementos = []
        self._inorden(self.raiz, elementos)
        print(" -> ".join(elementos) if elementos else "Árbol vacío")

    def __str__(self) -> str:
        """
        Representación en string (orden ascendente).
        """
        elementos = []
        self._inorden(self.raiz, elementos)
        return " -> ".join(elementos)

    def __len__(self):
        """
        Retorna el número de elementos del ABB.
        """
        return self._tamaño

    def __del__(self):
        """
        Destructor: limpia el árbol al eliminar el objeto.
        """
        self.limpie()
