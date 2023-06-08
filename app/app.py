from flask import Flask, request, render_template

app = Flask(__name__)

# Se definen tres diccionarios vacíos para almacenar el inventario, los clientes y los trabajadores
inventario = {}
clientes = []
trabajadores = {}

# La función agregar_suministros toma como argumentos el código, el nombre y el precio de un suministro
# y lo agrega al diccionario de inventario con el código como clave y un diccionario con el nombre y el precio como valor
def agregar_suministros(codigo, nombre, precio):
    inventario[codigo] = {'nombre': nombre, 'precio': precio}

# La función quitar_suministros toma como argumento el código de un suministro
# y lo elimina del diccionario de inventario utilizando el método pop
def quitar_suministros(codigo, nombre):
    if codigo in inventario:
        inventario.pop(codigo)
        return True
    else:
        for codigo_producto, producto in inventario.items():
            if producto['nombre'] == nombre:
                inventario.pop(codigo_producto)
                return True
    return False

# La función ordenar_por_nombre toma como argumento un elemento del diccionario de inventario
# y devuelve el valor del campo 'nombre' del diccionario asociado a ese elemento
def ordenar_por_nombre(item):
    return item[1]['nombre']

# La función ordenar_por_codigo toma como argumento un elemento del diccionario de inventario
# y devuelve la clave de ese elemento
def ordenar_por_codigo(item):
    return item[0]

# La función ordenar_suministros toma como argumento un criterio de ordenamiento (nombre o código)
# y devuelve una lista de tuplas con los elementos del diccionario de inventario ordenados según ese criterio
def ordenar_suministros(criterio):
    items = list(inventario.items())
    key_functions = {'nombre': ordenar_por_nombre, 'codigo': ordenar_por_codigo}
    key_function = key_functions.get(criterio)
    if key_function:
        items.sort(key=key_function)
    return items

# La función buscar_producto toma como argumento una cadena de búsqueda (código o nombre de producto)
# y devuelve el código del producto si lo encuentra en el diccionario de inventario o None si no lo encuentra
def buscar_producto(busqueda):
    for codigo, producto in inventario.items():
        if codigo == busqueda or producto['nombre'] == busqueda:
            return codigo
    return None

saldo_cuenta = 1000

# La función cobro_productos toma como argumento una lista de productos a cobrar (por código o nombre)
# e imprime un ticket con el detalle del cobro y realiza el cobro si hay suficiente saldo en la cuenta bancaria del cliente
def cobro_productos(lista_productos):
    global saldo_cuenta
    total = 0
    ticket = []
    for busqueda in lista_productos:
        codigo = buscar_producto(busqueda)
        if codigo:
            total += inventario[codigo]['precio']
            ticket.append(f"{codigo} - {inventario[codigo]['nombre']} - ${inventario[codigo]['precio']}")
        else:
            print(f"Producto no encontrado: {busqueda}")
    print("\nTicket de pago:")
    print("\n".join(ticket))
    print(f"\nTotal: ${total}\n")
    if total <= saldo_cuenta:
        cuenta_bancaria = input("Ingresa tu cuenta bancaria para realizar el pago: ")
        saldo_cuenta -= total
        print(f"\nSe ha realizado el cobro a la cuenta {cuenta_bancaria}\n")
        print(f"Saldo restante en la cuenta: ${saldo_cuenta}\n")
    else:
        print("No hay suficiente saldo en la cuenta para realizar el pago\n")

# La función atencion_clientes toma como argumentos el código de un producto y un mensaje del cliente
# y agrega un diccionario con esa información a la lista de clientes
def atencion_clientes(codigo_producto, mensaje):
    global clientes
    clientes.append({'codigo_producto': codigo_producto, 'mensaje': mensaje})

# La función alta_trabajador toma como argumentos el código, el nombre, el apellido y el puesto de un trabajador
# y lo agrega al diccionario de trabajadores con el código como clave y un diccionario con el nombre, apellido y puesto como valor
def alta_trabajador(codigo, nombre, apellido, puesto):
    trabajadores[codigo] = {'nombre': nombre, 'apellido': apellido, 'puesto': puesto}

# La función baja_trabajador toma como argumento el código de un trabajador
# y lo elimina del diccionario de trabajadores utilizando el método pop
def baja_trabajador(codigo):
    if codigo in trabajadores:
        trabajadores.pop(codigo)

# La función cambio_puesto toma como argumentos el código de un trabajador y su nuevo puesto
# y actualiza el valor del campo 'puesto' del diccionario asociado a ese trabajador en el diccionario de trabajadores
def cambio_puesto(codigo, nuevo_puesto):
    trabajadores[codigo]['puesto'] = nuevo_puesto

@app.route('/')
def menu():
    # Muestra el menú principal
    return render_template('menu.html')

@app.route('/inventario')
def menu_inventario():
    # Muestra el menú de administración de inventario
    return render_template('menu_inventario.html')

@app.route('/inventario/agregar', methods=['GET', 'POST'])
def agregar_suministro():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        agregar_suministros(codigo, nombre, precio)
        return render_template('agregar_suministro.html', success=True)
    else:
        return render_template('agregar_suministro.html')

@app.route('/inventario/quitar', methods=['GET', 'POST'])
def quitar_suministro():
    success = False
    not_found = False
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        nombre = request.form.get('nombre')
        if quitar_suministros(codigo, nombre):
            success = True
        else:
            not_found = True
    return render_template('quitar_suministros.html', success=success, not_found=not_found)

@app.route('/inventario/ordenar', methods=['GET', 'POST'])
def ordenar_suministros_view():
    if request.method == 'POST':
        criterio = request.form['criterio']
        ordenados = ordenar_suministros(criterio)
        return render_template('ordenar_suministros.html', ordenados=ordenados)
    else:
        return render_template('ordenar_suministros.html')

@app.route('/clientes')
def menu_clientes():
    # Muestra el menú de atención a clientes
    return render_template('menu_clientes.html')

@app.route('/clientes/cobrar', methods=['GET', 'POST'])
def cobrar_productos():
    if request.method == 'POST':
        lista_productos = request.form.getlist('productos')
        ticket, total = cobro_productos(lista_productos)
        return render_template('cobrar_productos.html', ticket=ticket, total=total)
    else:
        return render_template('cobrar_productos.html')

@app.route('/clientes/atender', methods=['GET', 'POST'])
def atender_cliente():
    if request.method == 'POST':
        codigo_producto = request.form['codigo_producto']
        mensaje = request.form['mensaje']
        atencion_clientes(codigo_producto, mensaje)
        return render_template('atender_cliente.html', success=True)
    else:
        return render_template('atender_cliente.html')

@app.route('/personal')
def menu_personal():
    # Muestra el menú de administración de personal
    return render_template('menu_personal.html')

@app.route('/personal/alta', methods=['GET', 'POST'])
def alta_personal():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        puesto = request.form['puesto']
        alta_trabajador(codigo, nombre, apellido, puesto)
        return render_template('alta_personal.html', success=True)
    else:
        return render_template('alta_personal.html')

@app.route('/personal/baja', methods=['GET', 'POST'])
def baja_personal():
    if request.method == 'POST':
        codigo = request.form['codigo']
        baja_trabajador(codigo)
        return render_template('baja_personal.html', success=True)
    else:
        return render_template('baja_personal.html')

# La función cambio_puesto_view maneja las solicitudes GET y POST para la ruta /personal/cambio_puesto
# Esta ruta permite al usuario cambiar el puesto de un trabajador
@app.route('/personal/cambio_puesto', methods=['GET', 'POST'])
def cambio_puesto():
    # Si la solicitud es de tipo POST (el usuario envió el formulario)
    if request.method == 'POST':
        # Se obtienen los valores de los campos del formulario
        codigo = request.form['codigo']
        nuevo_puesto = request.form['nuevo_puesto']
        # Se llama a la función cambio_puesto para actualizar el puesto del trabajador
        cambio_puesto(codigo, nuevo_puesto)
        # Se muestra una plantilla HTML indicando que el cambio fue realizado con éxito
        return render_template('cambio_puesto.html', success=True)
    else:
        # Si la solicitud es de tipo GET (el usuario está solicitando el formulario)
        # Se muestra una plantilla HTML con el formulario para cambiar el puesto de un trabajador
        return render_template('cambio_puesto.html')

if __name__ == '__main__':
    app.run()