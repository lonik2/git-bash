def decir_texto(textos, enviados):
    while textos:
        texto_actual = textos.pop()
        print(texto_actual)
        enviados.append(texto_actual)

textos = ['hola, todo bien', 'como te va', 'que haces']
enviados = []
decir_texto(textos, enviados)
print(textos)
print(enviados)