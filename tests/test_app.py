import unittest
from app import calcular_total


class TestCalcularTotal(unittest.TestCase):
    def test_compra_normal(self):
        self.assertEqual(calcular_total(1200, 3), 3600)

    def test_cantidad_cero(self):
        self.assertEqual(calcular_total(1200, 0), 0)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            calcular_total(-100, 2)


if __name__ == "__main__":
    unittest.main()
