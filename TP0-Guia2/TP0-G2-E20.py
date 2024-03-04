class Libro:
    def __init__(self, nombre, autor, precio, editorial):
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial 
        self.precio = precio

    def datoslibro(self):
        print("- El nombre del libro es:", self.nombre)
        print("- Su autor es:", self.autor)
        print("- La editorial es:", self.editorial)
        print("- Su precio actual es:", self.precio)

    def cambiarPrecio(self):
        self.precio = int(input("Ingrese a continuacion el nuevo precio del libro: "))
        print("Precio modificado con exito.")

libromomo = Libro("Las aventuras del Momo", "Geronimo Benavides", 20000, "Splinter")
libromomo.datoslibro()
libromomo.cambiarPrecio()
libromomo.datoslibro()