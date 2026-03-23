class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante(self):
        print(f"El restaurante se llama: {self.nombre}")
        print(f"Se especializan en: {self.tipo_cocina}")
    
    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre} acaba de abrir")

class PuestoDeHelados(Restaurante):
    def __init__(self, nombre, tipo_cocina, sabores):
        super().__init__(nombre, tipo_cocina)
        self.sabores = sabores
        
    def mostrar_sabores(self):
        print(f"Bienvenidos a {self.nombre}")
        print("Tenemos los siguientes sabores de helado disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")

lista_sabores = ["Dulce de Leche granizado", "Chocolate amargo", "Frutilla a la crema", "Limón"]
heladeria = PuestoDeHelados("Helados El Pingüino", "Heladería", lista_sabores)

heladeria.describir_restaurante()
heladeria.mostrar_sabores()