import contextlib
import io
import unittest

from app import calcular, main


class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(calcular("sumar", 10, 5), 15)

    def test_restar(self):
        self.assertEqual(calcular("restar", 10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(calcular("multiplicar", 10, 5), 50)

    def test_dividir(self):
        self.assertEqual(calcular("dividir", 10, 5), 2)

    def test_decimales_y_negativos(self):
        self.assertAlmostEqual(calcular("sumar", -1.5, 2.25), 0.75)

    def test_division_por_cero(self):
        with self.assertRaisesRegex(ValueError, "dividir por cero"):
            calcular("dividir", 10, 0)

    def test_operacion_desconocida(self):
        with self.assertRaisesRegex(ValueError, "no válida"):
            calcular("potencia", 2, 3)

    def test_entrada_no_finita(self):
        with self.assertRaisesRegex(ValueError, "finitos"):
            calcular("sumar", float("inf"), 1)

    def test_cli(self):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            codigo = main(["multiplicar", "7", "6"])
        self.assertEqual(codigo, 0)
        self.assertEqual(salida.getvalue().strip(), "Resultado: 42")


if __name__ == "__main__":
    unittest.main()
