numint: int = int(input("Ingrese el numero entero que desea sumar: "))
numfloat: float = float(input("Ingrese el numero flotante que desea sumar: "))
print(float(numint + numfloat))
print("- Se sumo el numero", numint, "de tipo", type(numint), "y se sumo el numero", numfloat, "de tipo", type(numfloat))