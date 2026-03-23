archivo = 'unmpi.txt'

try:
    with open(archivo) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    cumpleaños = input("ingresa tu cumpleaños en la forma ddmmaa: ")

    if cumpleaños in pi_string:
        print("tu cumpleaños aparece en los primeros un millón de dígitos de pi")
        
        posicion = pi_string.find(cumpleaños)
        print(f"se encuentra a partir de la posición {posicion} después del 3.")
    else:
        print("tu cumpleaños no aparece en el primer millón de dígitos de pi")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo {archivo}")
    print("Asegurate de tener el archivo de texto en la misma carpeta que tu código")