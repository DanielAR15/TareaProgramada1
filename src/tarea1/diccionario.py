from abc import ABC, abstractmethod

class Diccionario(ABC):
    """
    Clase abstracta Diccionario. Dicta los métodos que deben tener los diccionarios.
    
    """
    @abstractmethod
    def inserte(self, elemento):
        """
        Inserta un elemento. Puede ser repetido.
        """
        pass

    @abstractmethod
    def borre(self, elemento):
        """
        Elimina un elemento si existe.
        """
        pass

    @abstractmethod
    def limpie(self):
        """
        Elimina todos los elementos.
        """
        pass

    @abstractmethod
    def miembro(self, elemento)-> bool:
        """
        Verifica si un elemento pertenece al diccionario.
        """
        pass

    @abstractmethod
    def imprima(self):
        """
        Imprime todos los elementos.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Covierte el diccionario a cadena de caracteres.
        """
        pass
