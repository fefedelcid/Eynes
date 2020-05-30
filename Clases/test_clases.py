import unittest
from clases import Circulo
from math import pi

class TestClases(unittest.TestCase):
    def test_radioInvalido(self):
        self.assertRaises(ValueError, Circulo, 0)
        self.assertRaises(ValueError, Circulo, -1)
        self.assertRaises(TypeError, Circulo, '0')
        self.assertRaises(TypeError, Circulo, True)
        self.assertRaises(TypeError, Circulo, 4+3j)

    def test_radioValido(self):
        self.assertEqual(Circulo, type(Circulo(1)))


    def test_Area(self):
        self.assertAlmostEqual(Circulo(1).area(), pi)


    def test_Perimetro(self):
        self.assertAlmostEqual(Circulo(1).perimetro(), 2*pi)


if __name__ == '__main__':
    unittest.main()
