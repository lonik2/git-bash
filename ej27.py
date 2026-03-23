class Restaurante:
    
    def __init__ (self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante (self):
        print (f"El restarante se llama: {self.nombre}")
        print (f"Se especializan en: {self.tipo_cocina}")
    
    def abrir_restaurante (self):
        print (f"El restaurante {self.nombre} acaba de abrir")

restaurante = Restaurante("don julio", "asado")

print (f"Atributo nombre: {restaurante.nombre}")
print (f"Atributo tipo cocina: {restaurante.tipo_cocina}")

restaurante.describir_restaurante()
restaurante.abrir_restaurante()