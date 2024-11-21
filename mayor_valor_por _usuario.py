def mayor_valor(*args):
    if len(args) == 0:
        return "No se proporcionaron valores"
    return max(args)

entrada = input("Ingresa los números separados por espacio: ")
valores = [float(x) for x in entrada.split()]
resultado = mayor_valor(*valores)
print(f"El mayor valor ingresado es: {resultado}")
