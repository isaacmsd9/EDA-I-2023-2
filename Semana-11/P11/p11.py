def decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def fibonacci_inverso(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [1, 0]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[::-1]

def menu():
    print('\033\n[1;36mBienvenido, puede realizar las siguientes operaciones:\033[0m\n')
    print('\033[1;33m1 Conversion de bases\033[0m\n')
    print('\033[1;33m2 Serie de Fibonacci\033[0m\n')
    print('\033[1;33m3 Salir\033[0m\n')
    opcion = int(input('\033[1;34mIngrese la opcion: \033[0m'))
    if opcion == 1:
        n = int(input('\n\033[1;34mIngrese el número entero N: \033[0m'))
        print('\n\033[1;32m' + decimal_a_binario(n) + '\033[0m')
    elif opcion == 2:
        n = int(input('\n\033[1;34mIngrese el número entero N: \033[0m'))
        print('\n\033[1;32m' + ' '.join(map(str, fibonacci_inverso(n))) + '\033[0m')
    elif opcion == 3:
        exit()

def main():
    menu()

if __name__ == '__main__':
    main()
