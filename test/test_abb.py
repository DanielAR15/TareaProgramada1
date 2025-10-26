import unittest
from tarea1.abbpunteros import AbbPunteros
from tarea1.abbvectorheap import ABBVectorHeap


class TestAbbPunteros(unittest.TestCase):
    """Pruebas unitarias para la clase AbbPunteros."""

    def setUp(self):
        self.abb = AbbPunteros()
        self.elementos = ["pera", "manzana", "uva", "fresa", "kiwi"]

    def test_insercion_y_orden(self):
        for e in self.elementos:
            self.abb.inserte(e)
        resultado = str(self.abb)
        esperado = "fresa -> kiwi -> manzana -> pera -> uva"
        self.assertEqual(resultado, esperado)

    def test_miembro_existente(self):
        self.abb.inserte("pera")
        self.assertTrue(self.abb.miembro("pera"))

    def test_miembro_inexistente(self):
        self.abb.inserte("pera")
        self.assertFalse(self.abb.miembro("mango"))

    def test_borrado(self):
        self.abb.inserte("pera")
        self.abb.inserte("manzana")
        self.assertTrue(self.abb.borre("pera"))
        self.assertFalse(self.abb.miembro("pera"))

    def test_limpieza(self):
        for e in self.elementos:
            self.abb.inserte(e)
        self.abb.limpie()
        self.assertEqual(len(self.abb), 0)


class TestAbbVectorHeap(unittest.TestCase):
    """Pruebas unitarias para la clase ABBVectorHeap."""

    def setUp(self):
        self.abb = ABBVectorHeap(20)
        self.elementos = ["pera", "manzana", "uva", "fresa", "kiwi"]

    def test_insercion_y_orden(self):
        for e in self.elementos:
            self.abb.inserte(e)
        resultado = str(self.abb)
        esperado = "fresa -> kiwi -> manzana -> pera -> uva"
        self.assertEqual(resultado, esperado)

    def test_miembro_existente(self):
        self.abb.inserte("kiwi")
        self.assertTrue(self.abb.miembro("kiwi"))

    def test_miembro_inexistente(self):
        self.abb.inserte("pera")
        self.assertFalse(self.abb.miembro("naranja"))

    def test_borrado(self):
        self.abb.inserte("pera")
        self.abb.inserte("fresa")
        self.assertTrue(self.abb.borre("fresa"))
        self.assertFalse(self.abb.miembro("fresa"))

    def test_limpieza(self):
        for e in self.elementos:
            self.abb.inserte(e)
        self.abb.limpie()
        self.assertEqual(len(self.abb), 0)


if __name__ == "__main__":
    unittest.main()
