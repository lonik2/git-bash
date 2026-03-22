def sandwich_ingredientes (*ingredientes):
    print ("Se pidio un sandwich con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print (f"-{ingrediente}")

sandwich_ingredientes("jamon", "queso")
sandwich_ingredientes("pollo", "tomate", "lechuga")
sandwich_ingredientes("carne", "huevo", "queso", "rucula")