from tarea1.diccionario import Diccionario

class TablaHashAbierta(Diccionario):
    def __init__(self, capacidad: int = 10, factor_carga_max: float = 0.7):
        """
        Crea una tabla hash abierta (con encadenamiento).
        :param capacidad: tamaño inicial de la tabla.
        :param factor_carga_max: definicion de carga antes de redistribuir.
        """
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)]
        self.tamaño = 0
        self.factor_carga_max = factor_carga_max

    def _hash(self, elemento: str) -> int:
        """
        Función hash simple: suma de códigos ASCII módulo capacidad.
        """
        return sum(ord(c) for c in elemento) % self.capacidad

    def _factor_carga(self) -> float:
        return self.tamaño / self.capacidad

    def _rehash(self):
        """
        Redistribuye todos los elementos en una tabla más grande.
        """
        print(f"Capacidad anterior: {self.capacidad}")
        print(f"nueva capacidad: {self.capacidad * 2}")

        elementos = [elem for bucket in self.tabla for elem in bucket]
        self.capacidad *= 2
        self.tabla = [[] for _ in range(self.capacidad)]
        self.tamaño = 0

        for e in elementos:
            self.inserte(e)

    # ==============================
    # Métodos del Diccionario
    # ==============================
