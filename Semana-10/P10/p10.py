# Función para agregar un libro a la lista de libros
def agregar_libro(titulo, libros):
    libros += [titulo]

# Función para eliminar un libro de la lista de libros si está presente
def eliminar_libro(titulo, libros):
    if titulo in libros:
        libros[:] = [libro for libro in libros if libro != titulo]

# Función para ordenar la lista de libros en orden alfabético
def ordenar_biblioteca(libros):
    for i in range(len(libros)):
        for j in range(i + 1, len(libros)):
            if libros[i] > libros[j]:
                libros[i], libros[j] = libros[j], libros[i]

# Función para mostrar los libros registrados en la biblioteca
def ver_biblioteca(libros):
    for libro in libros:
        print(libro)

# Código principal
if __name__ == '__main__':
    libros = []  # Lista global para almacenar los libros de la biblioteca
    while True:  # Bucle principal del programa
        # Muestra el menú de opciones al usuario
        print("\nBienvenido a la biblioteca, puede realizar las siguientes operaciones:\n")
        print("1- Agregar libro")
        print("2- Eliminar libro")
        print("3- Ordenar biblioteca")
        print("4- Ver biblioteca")
        print("5- Salir")

        # Pide al usuario que ingrese una opción
        opcion = input("\nIngrese la opción: ")

        # Ejecuta la opción seleccionada por el usuario
        if opcion == "1":
            # Pide al usuario el título del libro a agregar
            titulo = input("\nIngrese el título del libro: ")
            agregar_libro(titulo, libros)
        elif opcion == "2":
            # Pide al usuario el título del libro a eliminar
            titulo = input("\nIngrese el título del libro: ")
            eliminar_libro(titulo, libros)
        elif opcion == "3":
            # Ordena la biblioteca en orden alfabético
            ordenar_biblioteca(libros)
            print("\nLa biblioteca ha sido ordenada.")
        elif opcion == "4":
            # Muestra los libros registrados en la biblioteca
            print("\nLibros registrados en la biblioteca:\n")
            ver_biblioteca(libros)
        elif opcion == "5":
            # Sale del menú y termina el programa
            break