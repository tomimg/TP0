class CuentaBancaria:
    def __init__(self, nombre, dni, balance):
        self.nombre = nombre
        self.dni = dni
        self.balance = balance

    def cuenta(self):
        print("- Cuenta bancaria de:", self.nombre, "|| DNI:", self.dni, "|| Balance actual:", self.balance, "ARS.")
        print("--------------------")

    def depositar(self):
        print("Actualmente se encuentra en la cuenta de:", self.nombre)
        self.balance += int(input("Ingrese el monto que desea depositar --> "))
        print("Su nuevo balance es:", self.balance, "ARS.")
        print("--------------------")

    def retirar(self):
        print("Actualmente se encuentra en la cuenta de:", self.nombre)
        self.balance -= int(input("Ingrese el monto que desea retirar --> "))
        print("Su nuevo balance es:", self.balance, "ARS.")
        print("--------------------")

retacon = CuentaBancaria("Napoleon", 1240670, 1000000)
pepebotellas = CuentaBancaria("Jose", 1239800, 1000)

retacon.cuenta()
pepebotellas.cuenta()
retacon.retirar()
pepebotellas.depositar()