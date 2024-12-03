def calculadora_basica():
    print("Bienvenido a la calculadora básica:")
    primer_num = float(input("Ingresa el primer número: "))
    segundo_num = float(input("Ingresa el segundo número: "))
    operacion = input("Selecciona una operación (+, -, *, /): ")

    if operacion == "+":
        print(f"El resultado es: {primer_num + segundo_num}")
    elif operacion == "-":
        print(f"El resultado es: {primer_num - segundo_num}")
    elif operacion == "*":
        print(f"El resultado es: {primer_num * segundo_num}")
    elif operacion == "/":
        if segundo_num != 0:
            print(f"El resultado es: {primer_num / segundo_num}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operación no reconocida.")

calculadora_basica()

import random
numero_secreto = random.randint(1, 100)
intento_usuario = -1

while intento_usuario != numero_secreto:
    intento_usuario = int(input("Adivina el número (entre 1 y 100): "))
    if intento_usuario < numero_secreto:
        print("El número es mayor...")
    elif intento_usuario > numero_secreto:
        print("El número es menor...")
    else:
        print("¡Felicidades! Has adivinado el número.")
