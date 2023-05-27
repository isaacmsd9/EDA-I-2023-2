# Función para agregar un libro
def agregar_libro(books): 
    titulo = input('Ingrese el título del libro: ') #un libro esta representado por su titulo
    books.append(titulo) 
    print('Libro agregado:', titulo)

# Función para eliminar un libro
def eliminar_libro(books):
    titulo = input('Ingrese el título del libro: ')
    if titulo in books:
        books.remove(titulo)
        print('Libro eliminado:', titulo)
    else:
        print('Libro no encontrado')

# Función para ordenar la biblioteca
def ordenar_biblioteca(books):
    books.sort()
    print('\nLa biblioteca queda con el siguiente orden:\n')
    for libro in books:
        print(libro)

# Función para ver la biblioteca
def ver_biblioteca(books): 
    print('\nLa biblioteca contiene los siguientes libros:\n')
    for libro in books: 
        print(libro)

# Código principal
if _name_ == '_main_':
    libros = [] 
    while True:
        print('\nBienvenido a la biblioteca, puede realizar las siguientes operaciones:\n')
        print('1 Agregar libro')
        print('2 Eliminar libro')
        print('3 Ordenar biblioteca')
        print('4 Ver biblioteca')
        print('5 Salir')
        option = input('\nIngrese la opción: ')
        
        if option == '1':
            agregar_libro(libros) 
        elif option == '2':
            eliminar_libro(libros)
        elif option == '3':
            ordenar_biblioteca(libros)
        elif option == '4':
            ver_biblioteca(libros)
        elif option == '5': 
            break