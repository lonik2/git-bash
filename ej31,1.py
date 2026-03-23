import random

opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

my_ticket = [1, 4, 6, 'D']
my_ticket.sort(key=str)

ganaste = False
intentos = 0

while not ganaste:
    intentos += 1
    ticket_ganador = random.sample(opciones, k=4)
    ticket_ganador.sort(key=str)

    if ticket_ganador == my_ticket:
        ganaste = True

print(f"El ticket ganador fue: {ticket_ganador}")
print(f"Se necesitaron {intentos} intentos para que tu boleto saliera ganador.")
