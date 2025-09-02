import random

print("¡Bienvenido a Adivina el Número!")
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    try:
        adivinanza = int(input("Ingresa un número entre 1 y 100: "))
        intentos += 1
        if adivinanza < numero_secreto:
            print("Muy bajo, intenta de nuevo.")
        elif adivinanza > numero_secreto:
            print("Muy alto, intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
    except ValueError:
        print("Por favor ingresa un número válido.")
