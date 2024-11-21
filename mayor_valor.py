def mayor_valor(*args):
    if len(args) == 0:
        return "No se proporcionaron valores"
    return max(args)

# Ejemplo de uso
print(mayor_valor(3, 5, 7, 2, 8))  # Devuelve 8
print(mayor_valor(10, 20, 5))      # Devuelve 20
print(mayor_valor())               # Devuelve "No se proporcionaron valores"
