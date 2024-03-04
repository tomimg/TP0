numero = int(input("Ingrese un numero: "))
factorial = 1

factorial *= numero
numero -= 1

while numero > 0:
    factorial *= numero
    numero -= 1

print("El factorial de su numero es:", factorial)