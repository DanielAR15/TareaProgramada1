from tarea1.diccionario import Diccionario

class TablaHashAbierta(Diccionario):
    def __init__(self, capacidad: int = 10, factor_carga_max: float = 0.7):
        """
        Inicializa una tabla hash abierta.
        """
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)]
        self.tamaño = 0
        self.factor_carga_max = factor_carga_max

    def _hash(self, elemento: str) -> int:
        """
        Calcula el índice hash de un elemento haciendo uso de DJB2.
        """
        h = 5381
        for c in elemento:
            h = ((h << 5) + h) + ord(c)  # h * 33 + ord(c)
        return h % self.capacidad


    def _factor_carga(self) -> float:
        """
        Calcula el factor de carga actual.
        """
        return self.tamaño / self.capacidad

    def _rehash(self):
        """
        Duplica la capacidad de la tabla y redistribuye todos los elementos.
        """
        print(f"Capacidad anterior: {self.capacidad}")
        print(f"Nueva capacidad: {self.capacidad * 2}")

        elementos = [elem for bucket in self.tabla for elem in bucket]
        self.capacidad *= 2
        self.tabla = [[] for _ in range(self.capacidad)]
        self.tamaño = 0

        for e in elementos:
            self.inserte(e)


    # ==============================
    # Métodos requeridos por Diccionario
    # ==============================

    def inserte(self, elemento: str):
        """
        Inserta un elemento en la tabla hash. Permite duplicados.
        """
        if self._factor_carga() > self.factor_carga_max:
            self._rehash()

        indice = self._hash(elemento)
        self.tabla[indice].append(elemento)
        self.tamaño += 1

    def borre(self, elemento: str) -> bool:
        """
        Elimina un elemento de la tabla si existe.
        """
        indice = self._hash(elemento)
        if elemento in self.tabla[indice]:
            self.tabla[indice].remove(elemento)
            self.tamaño -= 1
            return True
        return False

    def limpie(self):
        """
        Limpia la tabla hash, eliminando todos los elementos.
        """
        self.tabla = [[] for _ in range(self.capacidad)]
        self.tamaño = 0

    def miembro(self, elemento: str) -> bool:
        """
        Verifica si un elemento existe en la tabla.
        """
        indice = self._hash(elemento)
        return elemento in self.tabla[indice]

    def imprima(self):
        """
        Imprime el contenido de la tabla hash.
        """
        for i, bucket in enumerate(self.tabla):
            print(f"{i}: {bucket}")

    def __str__(self) -> str:
        """
        Representación en string de la tabla hash.
        """
        return str(self.tabla)

    def __len__(self):
        """
        Retorna el número total de elementos en la tabla.
        """
        return self.tamaño
