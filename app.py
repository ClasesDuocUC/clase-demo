def calcular_total(precio, cantidad):
    if precio < 0 or cantidad < 0:
        raise ValueError("Precio y cantidad no pueden ser negativos")
    return precio * cantidad


if __name__ == "__main__":
    print(f"Total: ${calcular_total(1200, 3)}")
