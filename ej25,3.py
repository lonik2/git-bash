def datos_auto (fabricante, modelo, **info_auto):
    info_auto["fabricante"] = fabricante
    info_auto["modelo"] = modelo
    return info_auto

auto = datos_auto ( "peugeot", "208",
                   color="gris",
                   año="2023")

print (auto)