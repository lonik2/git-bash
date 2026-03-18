fallecidos = ["a","b","c"]

for x in fallecidos:
    print (f"hola {x}, veni a cenar")

print ("c: no puedo.")

fallecidos[2] = "d"

print (f"oh,que mal.Vos podes {fallecidos[2]}?")

print ("invitare mas gente ya que la mesa es muy grande")

fallecidos.insert(0, "e")
fallecidos.insert(2, "f")
fallecidos.append("g")

print (f"{fallecidos[0]},{fallecidos[2]},{fallecidos[5]}, vienen?")
