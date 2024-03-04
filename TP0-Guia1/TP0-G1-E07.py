def esPrimo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

numero = int(input("Ingrese un numero: "))
if esPrimo(numero):
    print("Su numero es primo!")
else: 
    print("Su numero no es primo!")