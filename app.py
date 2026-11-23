"""Calculadora de cuatro operaciones para demostrar CI con GitHub Actions."""

import argparse
import math


def calcular(operacion: str, a: float, b: float) -> float:
    """Calcula usando dos números y una operación explícita."""
    operaciones = {
        "sumar": lambda x, y: x + y,
        "restar": lambda x, y: x - y,
        "multiplicar": lambda x, y: x * y,
        "dividir": lambda x, y: x / y,
    }
    if operacion not in operaciones:
        raise ValueError(f"Operación no válida: {operacion}")
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Los argumentos deben ser números finitos")
    if operacion == "dividir" and b == 0:
        raise ValueError("No se puede dividir por cero")
    return operaciones[operacion](a, b)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Calculadora de cuatro operaciones (demo de GitHub Actions)."
    )
    parser.add_argument("operacion", choices=["sumar", "restar", "multiplicar", "dividir"])
    parser.add_argument("a", type=float, help="Primer número")
    parser.add_argument("b", type=float, help="Segundo número")
    args = parser.parse_args(argv)
    try:
        resultado = calcular(args.operacion, args.a, args.b)
    except ValueError as exc:
        parser.error(str(exc))
    print(f"Resultado: {resultado:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
