nombres = ["a","b","admin", "c","d"]

if len(nombres) != 0:
    for x in nombres:
        if x == "admin":
            print ("hola admin, queres ver un informe?")
        else:
            print (f"hola {x}, gracias por iniciar sesion")
else:
    print ("se necesitan usuarios")
    