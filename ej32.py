nombre_archivo = 'unmpi.txt'

try:
    with open(nombre_archivo, 'r') as f:
        # 1. Leemos todo el contenido
        contenido_bruto = f.read()
        
        # 2. LIMPIEZA TOTAL: Nos quedamos SOLO con los números
        # Quitamos puntos, comas, saltos de línea (\n) y espacios
        pi_string = ""
        for caracter in contenido_bruto:
            if caracter.isdigit():
                pi_string += caracter
        
        # Si el archivo empezaba con 3.14..., ahora pi_string es "314159..."
        # Le quitamos el "3" inicial para buscar solo en los decimales
        if pi_string.startswith('3'):
            pi_string = pi_string[1:]

    # Verificamos largo del archivo
    print(f"Total de dígitos decimales cargados: {len(pi_string)}")

    busqueda = "010610"
    
    if busqueda in pi_string:
        posicion = pi_string.find(busqueda)
        print(f"¡ENCONTRADO! La secuencia {busqueda} está en la posición {posicion}.")
    else:
        print(f"La secuencia {busqueda} NO se encontró.")
        # Te doy una pista de los primeros dígitos para ver si el archivo es correcto
        print(f"Primeros 20 dígitos en tu archivo: {pi_string[:20]}")

except FileNotFoundError:
    print("No se encontró el archivo 'unmpi.txt'.")