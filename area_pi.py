import math

def area_circulo(radio):
    return math.pi * radio ** 2

radio_usuario = float(input("Ingresa el radio del círculo: "))
area = area_circulo(radio_usuario)
print(f"El área del círculo con radio {radio_usuario} es: {area}")
