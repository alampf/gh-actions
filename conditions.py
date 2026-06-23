import os

edad = int(os.getenv("EDAD", 0))
nombre = os.getenv("NOMBRE", "Desconocido")

if edad >= 18:
    print(f"{nombre} es mayor de edad")
else:
    print(f"{nombre} es menor de edad")