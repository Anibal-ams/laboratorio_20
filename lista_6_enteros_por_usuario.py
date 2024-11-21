# Función que recibe una lista y retorna la suma de todos sus elementos
def suma_lista(lista):
    return sum(lista)

# Función que recibe una lista y retorna el mayor valor
def mayor_valor(lista):
    return max(lista)

# Función que recibe una lista y retorna el menor valor
def menor_valor(lista):
    return min(lista)

# Bloque principal
if __name__ == "__main__":
    # Solicitar al usuario que ingrese 6 enteros
    lista_enteros = []
    for i in range(6):
        num = int(input(f"Ingrese el número {i+1}: "))
        lista_enteros.append(num)

    # Calcular y mostrar la suma
    suma = suma_lista(lista_enteros)
    print(f"La suma de los elementos de la lista es: {suma}")
    
    # Calcular y mostrar el mayor valor
    mayor = mayor_valor(lista_enteros)
    print(f"El mayor valor de la lista es: {mayor}")
    
    # Calcular y mostrar el menor valor
    menor = menor_valor(lista_enteros)
    print(f"El menor valor de la lista es: {menor}")
