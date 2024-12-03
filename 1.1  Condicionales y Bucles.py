
numero_usuario = int(input("Introduce un número: "))
if numero_usuario % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


lista_numeros = [1, 2, 3, 4, 5]
for numero in lista_numeros:
    print(f"El cuadrado de {numero} es {numero**2}")


entrada_usuario = ""
while entrada_usuario != "0":
    entrada_usuario = input("Introduce un número (0 para salir): ")
    print(f"Has introducido: {entrada_usuario}")
