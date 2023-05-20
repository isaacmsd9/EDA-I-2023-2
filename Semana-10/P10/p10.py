class Biblioteca:
    def __init__(self):
        # Inicializa la lista de libros
        self.libros = []

    def agregar_libro(self, titulo):
        # Agrega un libro a la lista de libros
        self.libros.append(titulo)

    def eliminar_libro(self, titulo):
        # Elimina un libro de la lista de libros si está presente
        if titulo in self.libros:
            self.libros.remove(titulo)

    def ordenar_biblioteca(self):
        # Ordena la lista de libros en orden alfabético 
        for i in range(len(self.libros)):
            for j in range(i + 1, len(self.libros)):
                if self.libros[i] > self.libros[j]:
                    self.libros[i], self.libros[j] = self.libros[j], self.libros[i]

    def ver_biblioteca(self):
        
        # Muestra los libros registrados en la biblioteca
        
        for libro in self.libros:
        
            print(libro)

if __name__ == "__main__":
    
    # Crea una instancia de la clase Biblioteca
    
    biblioteca = Biblioteca()
    
    while True:
        
        # Muestra el menú de opciones al usuario
        
        print("\nBienvenido a la biblioteca, puede realizar las siguientes operaciones:\n")
        print("1- Agregar libro")
        print("2- Eliminar libro")
        print("3- Ordenar biblioteca")
        print("4- Ver biblioteca")
        print("5- Salir")
        
        opcion = input("\nIngrese la opción: ")
        if opcion == "1":
            # Pide al usuario el título del libro a agregar
            titulo = input("\nIngrese el título del libro: ")
            biblioteca.agregar_libro(titulo)
        elif opcion == "2":
            # Pide al usuario el título del libro a eliminar
            titulo = input("\nIngrese el título del libro: ")
            biblioteca.eliminar_libro(titulo)
        elif opcion == "3":
            # Ordena la biblioteca en orden alfabético
            biblioteca.ordenar_biblioteca()
            print("\nLa biblioteca ha sido ordenada.")
        elif opcion == "4":
            # Muestra los libros registrados en la biblioteca
            print("\nLibros registrados en la biblioteca:\n")
            biblioteca.ver_biblioteca()
        elif opcion == "5":
            # Sale del menú y termina el programa
            break