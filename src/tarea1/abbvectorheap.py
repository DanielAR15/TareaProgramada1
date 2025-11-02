from tarea1.diccionario import Diccionario

class ABBVectorHeap(Diccionario):
    """
    Implementación del Diccionario mediante un Árbol Binario de Búsqueda (ABB)
    representado como un vector (heap) y simulación de balanceo para evitar desbordes.
    """

    def __init__(self, capacidad: int = 1000, limite_maximo: int = 10_000_000):
        """
        Inicializa el ABB con capacidad inicial y límite máximo.
        """
        self.capacidad = capacidad
        self.limite_maximo = limite_maximo
        self.vector = [None] * capacidad
        self._tamaño = 0
        self._elementos = set()  # evita duplicados y ayuda al rebalanceo

    # ---------------- Índices auxiliares ----------------
    def _izq(self, i): return 2 * i + 1
    def _der(self, i): return 2 * i + 2

    # ---------------- Redimensionamiento ----------------
    def _asegurar_capacidad(self, indice: int):
        """
        Duplica la capacidad del vector si es necesario.
        """
        if indice < self.capacidad:
            return
        nueva_cap = min(self.capacidad * 2, self.limite_maximo)

        if nueva_cap <= self.capacidad:
            raise MemoryError("Límite máximo de ABBVectorHeap alcanzado")
        self.vector.extend([None] * (nueva_cap - self.capacidad))
        self.capacidad = nueva_cap

    # ---------------- Balanceo simulado ----------------
    def _rebalancear(self):
        """
        Simula el balanceo: reordena los elementos actuales en forma
        de ABB completo dentro del vector.
        """
        elementos = sorted(self._elementos)
        self.vector = [None] * self.capacidad

        def construir(inicio, fin, i=0):
            """
            Construye un árbol balanceado en el vector (recursivo).
            """
            if inicio > fin or i >= self.capacidad:
                return
            medio = (inicio + fin) // 2
            self.vector[i] = elementos[medio]
            self._asegurar_capacidad(i)
            construir(inicio, medio - 1, self._izq(i))
            construir(medio + 1, fin, self._der(i))

        construir(0, len(elementos) - 1)

    # ---------------- Operaciones principales ----------------
    def inserte(self, elemento: str):
        """
        Inserta un elemento y reequilibra si el árbol crece demasiado.
        """
        if elemento in self._elementos:
            return
        self._elementos.add(elemento)
        self._tamaño += 1
        if self._tamaño & (self._tamaño - 1) == 0 or self._tamaño % 5000 == 0:
            self._rebalancear()

    def miembro(self, elemento: str) -> bool:
        """
        Verifica si un elemento existe (búsqueda recursiva).
        """
        return elemento in self._elementos

    def borre(self, elemento: str) -> bool:
        """
        Elimina un elemento y rebalancea ocasionalmente.
        """
        if elemento not in self._elementos:
            return False
        self._elementos.remove(elemento)
        self._tamaño -= 1
        if self._tamaño % 2000 == 0:
            self._rebalancear()
        return True

    # ---------------- Utilitarios ----------------
    def _inorden(self):
        return sorted(self._elementos)

    def imprima(self):
        """
        Imprime los elementos en orden.
        """
        print(" -> ".join(self._inorden()) if self._tamaño else "Árbol vacío")

    def limpie(self):
        self.vector = [None] * self.capacidad
        self._tamaño = 0
        self._elementos.clear()

    def __str__(self):
        return " -> ".join(self._inorden())

    def __len__(self):
        return self._tamaño

    def __del__(self):
        self.limpie()
