class CuentaBancaria:
    def __init__(self, nombre, dni, balance):
        self.nombre = nombre
        self.dni = dni
        self.balance = balance

    def getBalance(self):
        return self.balance

    def setNombre(self, nom):
        self.nombre = nom
    
    def getNombre(self):
        return self.nombre
    
retacon = CuentaBancaria("Napoleon", 1240670, 1000000)
pepebotellas = CuentaBancaria("Jose", 1239800, 1000)

print("El saldo actual de la cuenta es:", retacon.getBalance(), "ARS.")
pepebotellas.setNombre(str(input("Ingrese el nuevo nombre de la cuenta: ")))
print("El nuevo nombre de la cuenta es:", pepebotellas.getNombre())