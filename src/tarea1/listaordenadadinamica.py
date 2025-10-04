from tarea1.diccionario import Diccionario

class Nodo:
    def __init__(self, elemento:str=''):
        self.elemento = elemento
        self.siguiente: Nodo | None = None

class ListaOrdenadaDinámica(Diccionario):
    def __init__(self):
        self.__cabeza = Nodo()
        self.__tamaño = 0

    def __len__(self):
        return self.__tamaño
    
    def __getitem__(self, indice):

        """
        Permite acceder a un elemento por índice
        """

        if indice < 0 or indice >= self.__tamaño:
            raise IndexError("Índice fuera de rango")
        actual = self.__cabeza.siguiente
        for _ in range(indice):
            actual = actual.siguiente
        return actual.elemento  

    # Metodoos del diccionario ---------------------------

    def inserte(self, elemento):

        """
        Inserta el elemento en orden ascendente
        """
        
        referencia: Nodo = self.__cabeza
        
        while referencia.siguiente is not None and referencia.siguiente.elemento < elemento:
            referencia = referencia.siguiente

        nodo = Nodo(elemento)
        nodo.siguiente = referencia.siguiente
        referencia.siguiente = nodo
        self.__tamaño += 1

    def borre(self, elemento):

        """
        Borra un elemento si existe.
        """

        referencia: Nodo = self.__cabeza
        while referencia.siguiente is not None and referencia.siguiente.elemento != elemento:
            referencia = referencia.siguiente
        if referencia.siguiente is not None:
            referencia.siguiente = referencia.siguiente.siguiente
            self.__tamaño -= 1
            return True
        return False

    def limpie(self):

        """
        Elimina todos los elementos de un diccionario.
        """

        self.__cabeza.siguiente = None
        self.__tamaño = 0
        pass

    def miembro(self, elemento):
        referencia: Nodo = self.__cabeza.siguiente
        while referencia is not None:
            if referencia.elemento == elemento:
                return True
            elif referencia.elemento > elemento:
                return False
            referencia = referencia.siguiente
        return False
    
    def imprima(self):
        """
        Imprime todos los elementos de la lista.
        """
        actual = self.__cabeza.siguiente
        salida = []
        while actual is not None:
            salida.append(actual.elemento)
            actual = actual.siguiente
        print(" -> ".join(salida) if salida else "Diccionario vacío")
        
    def __str__(self) -> str:
        """
        Representación en string de la lista.
        """
        elementos = []
        actual = self.__cabeza.siguiente
        while actual is not None:
            elementos.append(actual.elemento)
            actual = actual.siguiente
        return " -> ".join(elementos)
        
    
    def __del__(self):
        """
        Destructor: limpia la lista cuando se elimina el objeto.
        """
        self.limpie()
