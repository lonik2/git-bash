frutas = ["bananas", "frutillas", "manzanas"]
frutas_amigo = ["naranjas", "sandias", "manzanas"]

for x in frutas:
    for y in frutas_amigo:
        if x == y:
            print (f"te gustan las {x} como a mi")