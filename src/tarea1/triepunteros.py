from tarea1.diccionario import Diccionario

class NodoTrie:
    """
    Nodo para el Trie con punteros.
    """
    
    def __init__(self):
        self.hijos = {}
        self.fin_de_palabra = False

class TriePunteros(Diccionario):
    """
    Trie usando punteros y diccionarios para los hijos.
    """
    def __init__(self):
        self.raiz = NodoTrie()
        self.contador = 0
    
    def inserte(self, hilera):
        """
        Inserta una hilera en el Trie.
        """
        nodo_actual = self.raiz
        
        for caracter in hilera:
            if caracter not in nodo_actual.hijos:
                nodo_actual.hijos[caracter] = NodoTrie()
            nodo_actual = nodo_actual.hijos[caracter]
        
        if not nodo_actual.fin_de_palabra:
            nodo_actual.fin_de_palabra = True
            self.contador += 1
    
    def borre(self, hilera):
        """
        Borra una hilera del Trie.
        """
        nodo_actual = self.raiz
        pila = []
        
        for caracter in hilera:
            if caracter not in nodo_actual.hijos:
                return False
            pila.append((caracter, nodo_actual))
            nodo_actual = nodo_actual.hijos[caracter]
        
        if not nodo_actual.fin_de_palabra:
            return False
        
        nodo_actual.fin_de_palabra = False
        self.contador -= 1
        
        self._limpiar_nodos(pila, nodo_actual)
        
        return True
    
    def _limpiar_nodos(self, pila, nodo_actual):
        """
        Limpia nodos que ya no son necesarios.
        """
        if nodo_actual.hijos or nodo_actual.fin_de_palabra:
            return
        
        while pila:
            caracter, nodo_padre = pila.pop()
            
            if caracter in nodo_padre.hijos:
                del nodo_padre.hijos[caracter]
            
            if nodo_padre.hijos or nodo_padre.fin_de_palabra:
                break
    
    def miembro(self, hilera):
        """
        Verifica si una hilera existe en el Trie.
        """
        nodo_actual = self.raiz
        
        for caracter in hilera:
            if caracter not in nodo_actual.hijos:
                return False
            nodo_actual = nodo_actual.hijos[caracter]
        
        return nodo_actual.fin_de_palabra
    
    def imprima(self):
        """
        Imprime todas las hileras en orden alfabético.
        """
        if self.contador == 0:
            print("El Trie está vacío")
            return
        
        print(f"Posee {self.contador} elementos:")
        self._imprimir_recursivo(self.raiz, "")
    
    def _imprimir_recursivo(self, nodo, prefijo):
        """
        Función recursiva para poder imprimir el trie.
        """
        if nodo.fin_de_palabra:
            print(f"  {prefijo}")
        
        for caracter in sorted(nodo.hijos.keys()):
            self._imprimir_recursivo(nodo.hijos[caracter], prefijo + caracter)

    def juntar_elementos(self, nodo, prefijo, elementos):
        """
        Colecta todos los elementos del trie recursivamente.
        """
        if nodo.fin_de_palabra:
            elementos.append(prefijo)
            
        for caracter in nodo.hijos:
            self.juntar_elementos(nodo.hijos[caracter], prefijo + caracter, elementos) 
    
    def limpie(self):
        """
        Limpia todo el Trie.
        """
        self.raiz = NodoTrie()
        self.contador = 0

    def __str__(self):
        """
        Devuelve una representación en string del Trie.
        """
        elementos = []
        self.juntar_elementos(self.raiz, "", elementos)
        return f"TriePunteros({', '.join(sorted(elementos))})"

    def __len__(self):
        """
        Devuelve el número de elementos en el Trie.
        """
        return self.contador