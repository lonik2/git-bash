edad = 0

while True:
    edad = (input ("Escriba su edad(escriba salir para terminar el programa):"))
    if edad == "salir":
        break
    else:
        if edad < "3":
            print ("su entrada es gratis")
        if edad == "3" and edad <= "12":
            print ("su entrada cuesta $10")
        if edad > "12":
            print ("su entrada cuesta $15")