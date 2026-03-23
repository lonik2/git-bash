class Restaurante:
    
    def __init__ (self, nombre, tipo_cocina, num_empleados):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.num_empleados = num_empleados
    
    def describir_restaurante (self):
        print (f"El restarante se llama: {self.nombre}")
        print (f"Se especializan en: {self.tipo_cocina}")
        print (f"Tienen {self.num_empleados} empleados")
    
    def abrir_restaurante (self):
        print (f"El restaurante {self.nombre} acaba de abrir")

restaurante = Restaurante("don julio", "asado", "20")
restaurante2 = Restaurante("Belgrano", "Criollo", "10")

print (f"Atributo nombre: {restaurante.nombre}")
print (f"Atributo tipo cocina: {restaurante.tipo_cocina}")
print (f"Atributo num empleados: {restaurante.num_empleados}")

restaurante.describir_restaurante()
restaurante.abrir_restaurante()

print("-------------------------------")

print (f"Atributo nombre: {restaurante2.nombre}")
print (f"Atributo tipo cocina: {restaurante2.tipo_cocina}")
print (f"Atributo num empleados: {restaurante2.num_empleados}")

restaurante2.describir_restaurante()
restaurante2.abrir_restaurante()