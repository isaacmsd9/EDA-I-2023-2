def decimal_a_binario(n):
    """
    Convierte un número decimal a binario de forma recursiva.

    Args:
        n (int): El número decimal a convertir.

    Returns:
        str: El número binario resultante.
    """
    if n == 0:
        # Caso base: si n es 0, se devuelve una cadena vacía
        return ''
    else:
        # Caso recursivo: se divide n entre 2 y se concatena el residuo al resultado de la llamada recursiva
        return decimal_a_binario(n // 2) + str(n % 2)

def fibonacci(n):
    """
    Devuelve los primeros N términos de la serie de Fibonacci usando recursión.

    Args:
        n (int): El número de términos a devolver.

    Returns:
        list: Una lista con los primeros N términos de la serie de Fibonacci.
    """
    if n == 0:
        # Caso base: si n es 0, se devuelve una lista vacía
        return []
    elif n == 1:
        # Caso base: si n es 1, se devuelve una lista con el primer término de la serie
        return [0]
    elif n == 2:
        # Caso base: si n es 2, se devuelve una lista con los dos primeros términos de la serie
        return [0, 1]
    else:
        # Caso recursivo: se obtienen los primeros n-1 términos y se agrega el siguiente término al final
        fib = fibonacci(n - 1)
        fib.insert(fib[0] + fib[1])
        return fib

if __name__ == '__main__':
    # Este bloque de código solo se ejecuta si el archivo se ejecuta como un script
    while True:
        # Muestra un menú de opciones al usuario
        print('\n\033[1;36mBienvenido, puede realizar las siguientes operaciones:\033[0m\n')
        print('\033[1;33m1 Conversion de bases\033[0m\n')
        print('\033[1;33m2 Serie de Fibonacci\033[0m\n')
        print('\033[1;33m3 Salir\033[0m\n')
        
        # Pide al usuario que ingrese una opción
        opcion = int(input('\033[1;34mIngrese la opcion: \033[0m'))
        
        if opcion == 1:
            # Si el usuario eligió la opción 1, se pide un número entero y se muestra su representación binaria
            n = int(input('\n\033[1;34mIngrese el número entero N: \033[0m'))
            print('\n\033[1;32m' + decimal_a_binario(n) + '\033[0m')
            
        elif opcion == 2:
            # Si el usuario eligió la opción 2, se pide un número entero y se muestran los primeros N términos de la serie de Fibonacci
            n = int(input('\n\033[1;34mIngrese el número entero N: \033[0m'))
            print('\n\033[1;32m' + ' '.join(map(str, fibonacci(n)[::-1])) + '\033[0m')
            
        elif opcion == 3:
            # Si el usuario eligió la opción 3, se termina el programa
            exit()