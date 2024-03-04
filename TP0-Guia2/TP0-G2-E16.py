class Persona: 
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    
    def atributos(self):
        print("Me llamo", self.nombre, "tengo", self.edad, "años y mido", self.altura, "m.")

ramon = Persona("Ramon Benavides", 23, 1.75)
rongoat = Persona("Salomon Rondon", 34, 1.89)
ramon.atributos()
rongoat.atributos()