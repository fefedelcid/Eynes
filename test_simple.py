import unittest
import simple

class TestSimple(unittest.TestCase):

    def test_Lista(self):
        lista = simple.simple()
        self.assertEqual(type(lista), list)
        self.assertEqual(len(lista), 10)


    def test_OrdenarLista(self):
        lista = simple.simple()
        l_ord = simple.ordenar(lista)

        joven = l_ord[0]["edad"]
        viejo = l_ord[-1]["edad"]

        self.assertGreater(viejo, joven)


    def test_OrdenarAleatorio(self):
        lista_ord = simple.ordenar()

        joven = lista_ord[0]["edad"]
        viejo = lista_ord[-1]["edad"]

        self.assertEqual(joven<viejo, True)


if __name__ == '__main__':
    unittest.main()
