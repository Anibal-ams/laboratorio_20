def mascaracteres(palabras):
    # Encontrar la palabra con más caracteres
    palabra_max = palabras[0]  # Empezamos con la primera palabra
    for palabra in palabras:
        if len(palabra) > len(palabra_max):  # Si encontramos una palabra más larga
            palabra_max = palabra
    return palabra_max

# Bloque principal
if __name__ == "__main__":
    # Lista de palabras
    palabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
    
    # Llamada a la función y mostrar el resultado
    print("Palabra con más caracteres:", mascaracteres(palabras))
