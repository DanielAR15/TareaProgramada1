from tarea1.tablahashabierta import TablaHashAbierta

class TablaHash(TablaHashAbierta):
    def __init__(self, tamaño=100):
        super().__init__(tamaño)
    
    def __str__(self):
        return str(self.diccionario)
    
    def inserte(self, hilera):
        super().inserte(hilera)
    
    def borre(self, hilera):
        return super().borre(hilera)
    
    def imprima(self):
        super().imprima()
    
    def limpie(self):
        super().limpie()
    
    def miembro(self, hilera):
        return super().miembro(hilera)
