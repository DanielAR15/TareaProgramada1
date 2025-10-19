from tarea1.diccionario import Diccionario

class ABBVectorHeap(Diccionario):
    """
    Implementación del Diccionario mediante un Árbol Binario de Búsqueda (ABB)
    representado como un vector o arreglo (heap).
    """

    def __init__(self, capacidad: int = 100):
        """
        Inicializa el ABB con una capacidad fija (por defecto 100).
        Las posiciones vacías se inicializan como None.
        """
        self.capacidad = capacidad
        self.vector = [None] * capacidad
        self._tamaño = 0

    
    # métodos  ---------------------------


    def _indice_izquierdo(self, i: int) -> int:
        """
        Devuelve el índice del hijo izquierdo.
        """
        return 2 * i + 1

    def _indice_derecho(self, i: int) -> int:
        """
        Devuelve el índice del hijo derecho.
        """
        return 2 * i + 2

    def _insertar_rec(self, i: int, elemento: str):
        """
        Inserta recursivamente un elemento en el ABB (versión por vector).
        """
        if i >= self.capacidad:
            raise IndexError("Capacidad del ABBVectorHeap excedida")

        if self.vector[i] is None:
            self.vector[i] = elemento
            self._tamaño += 1
        elif elemento < self.vector[i]:
            self._insertar_rec(self._indice_izquierdo(i), elemento)
        elif elemento > self.vector[i]:
            self._insertar_rec(self._indice_derecho(i), elemento)
        # Si el elemento ya existe, no se inserta (sin duplicados)

    def _buscar_rec(self, i: int, elemento: str) -> bool:
        """
        Busca recursivamente un elemento en el ABB.
        """
        if i >= self.capacidad or self.vector[i] is None:
            return False
        if elemento == self.vector[i]:
            return True
        elif elemento < self.vector[i]:
            return self._buscar_rec(self._indice_izquierdo(i), elemento)
        else:
            return self._buscar_rec(self._indice_derecho(i), elemento)

    def _inorden_rec(self, i: int, resultado: list[str]):
        """
        Recorrido inorden para imprimir los elementos en orden ascendente.
        """
        if i >= self.capacidad or self.vector[i] is None:
            return
        self._inorden_rec(self._indice_izquierdo(i), resultado)
        resultado.append(self.vector[i])
        self._inorden_rec(self._indice_derecho(i), resultado)

    def _eliminar_rec(self, i: int, elemento: str):
        """
        Elimina un elemento (versión simplificada, marca la posición como None).
        Nota: No reorganiza el árbol — enfoque educativo, no balanceado.
        """
        if i >= self.capacidad or self.vector[i] is None:
            return

        if elemento < self.vector[i]:
            self._eliminar_rec(self._indice_izquierdo(i), elemento)
        elif elemento > self.vector[i]:
            self._eliminar_rec(self._indice_derecho(i), elemento)
        else:
            # Marca el nodo como vacío
            self.vector[i] = None
            self._tamaño -= 1

   
    # métodos del diccionario ---------------------------
   

    def inserte(self, elemento: str):
        """
        Inserta un elemento en el árbol representado por vector.
        """
        self._insertar_rec(0, elemento)

    def borre(self, elemento: str) -> bool:
        """
        Elimina un elemento del árbol
        """
        if not self.miembro(elemento):
            return False
        self._eliminar_rec(0, elemento)
        return True

    def miembro(self, elemento: str) -> bool:
        """
        Verifica si un elemento existe en el árbol.
        """
        return self._buscar_rec(0, elemento)

    def limpie(self):
        """
        Limpia todo el árbol.
        """
        self.vector = [None] * self.capacidad
        self._tamaño = 0

    def imprima(self):
        """
        Imprime el árbol en orden ascendente.
        """
        elementos = []
        self._inorden_rec(0, elementos)
        print(" -> ".join(elementos) if elementos else "Árbol vacío")

    def __str__(self) -> str:
        """
        Representación en string de los elementos en orden.
        """
        elementos = []
        self._inorden_rec(0, elementos)
        return " -> ".join(elementos)

    def __len__(self):
        """
        Devuelve el número de elementos almacenados.
        """
        return self._tamaño

    def __del__(self):
        """
        Destructor: limpia el árbol al eliminar el objeto.
        """
        self.limpie()
