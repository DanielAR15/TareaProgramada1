from tarea1.diccionario import Diccionario

class Array:
    def __init__(self, valor_inicial=None, tamaño = None):
        """
        Inicializa el arreglo con un valor inicial o con una lista dada.
        """
        if not isinstance(tamaño, int) or tamaño < 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
        if not isinstance(valor_inicial, list):
            self.__lista = [valor_inicial] * tamaño
            self.__tamaño = tamaño
        else:
            self.__lista = valor_inicial
            self.__tamaño = len(valor_inicial)        

    def __getitem__(self, índice):
        """
        Devuelve el elemento en el índice dado.
        """
        if not (0 <= índice < self.__tamaño):
            raise IndexError("Índice de arreglo fuera de los límites.")
        return self.__lista[índice]

    def __setitem__(self, índice, value):
        """
        Asigna un valor en el índice dado.
        """
        if not (0 <= índice < self.__tamaño):
            raise IndexError("Índice de arreglo fuera de los límites")
        self.__lista[índice] = value

    def __len__(self):
        """
        Devuelve el tamaño del arreglo.
        """
        return self.__tamaño

    def __repr__(self):
        return f"Array({self.__lista})"
    
    def __str__(self) -> str:
        return str(self.__lista)

class ListaOrdenadaEstática(Diccionario):
    def __init__(self, tamaño):
        """
        Inicializa la lista ordenada estática con un tamaño fijo.
        """
        self.__arreglo: Array = Array(valor_inicial=None, tamaño=tamaño)
        self.__último: int | None = None

    def __len__(self):
        """
        Devuelve la cantidad de elementos actuales en la lista estática.
        """
        if self.__último is None:
            return 0
        else:
            return self.__último + 1
    
    def __getitem__(self, índice):
        """
        Devuelve el elemento en un índice específico.
        """
        if not (0 <= índice <= self.__último):
            raise IndexError("Índice de arreglo fuera de los limites")
        return self.__arreglo[índice]

    def inserte(self, elemento):
        """
        Inserta el elemento deseado en orden ascendente.
        """
        if self.__último is None:
            if len(self.__arreglo) == 0:
                raise ValueError("El arreglo está lleno")
            self.__arreglo[0] = elemento
            self.__último = 0
            return
        
        if self.__último +1 >= len(self.__arreglo):
            raise OverflowError("La lista está llena")
        
        pos = 0
        while pos <= self.__último and self.__arreglo[pos] < elemento:
            pos += 1
        
        for i in range(self.__último, pos -1, -1):
            self.__arreglo[i + 1] = self.__arreglo[i]
        
        self.__arreglo[pos] = elemento
        self.__último +=1

    def borre(self, elemento):
        """
        Elimina un elemento de la lista si existe.
        """
        if self.__último is None:
            return False
        
        pos = -1
        for i in range(self.__último + 1):
            if self.__arreglo[i] == elemento:
                pos = i
                break

        if pos == -1:
            return False
        
        for i in range(pos, self.__último):
            self.__arreglo[i] = self.__arreglo[i + 1]
        
        self.__arreglo[self.__último] = None
        self.__último -= 1

        if self.__último == -1:
            self.__último = None 

        return True

    def limpie(self):
        """
        Elimina todos los elementos de la lista estática.
        """
        if self.__último is not None:
            for i in range(self.__último + 1):
                self.__arreglo[i] = None
            self.__último = None

    def miembro(self, elemento):
        """
        Verifica si un elemento pertenece a la lista.
        """
        if self.__último is None:
            return False
                
        inicio, fin = 0, self.__último
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.__arreglo[medio] == elemento:
                return True
            elif self.__arreglo[medio] < elemento:
                inicio = medio + 1
            else:
                fin = medio - 1
        return False

    def imprima(self):
        """
        Imprime el contenido de la lista.
        """
        print(self)

    def __str__(self) -> str:
        """
        Convierte todo el contenido del arreglo en una hilera de string.
        """
        if self.__último is None:
            return "El diccionario está vacío"
        return str(self.__arreglo._Array__lista[:self.__último + 1])
    
    def __del__(self):
        """
        Destructor de la lista.
        """
        self.limpie()
        del self.__arreglo