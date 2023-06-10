# Importamos las clases y funciones necesarias del módulo Flask para crear una aplicación web
from flask import Flask, request, render_template, url_for, redirect

# Creamos una instancia de la clase Flask y la asignamos a la variable app
app = Flask(__name__)

# Definimos variables globales para almacenar información sobre el inventario, los clientes y los trabajadores
inventario = {}
clientes = []
trabajadores = {}

# Definimos una función para agregar suministros al inventario
def agregar_suministros(codigo, nombre, precio):
    # Agregamos el suministro al diccionario inventario con el código como clave y un diccionario con el nombre y el precio como valor
    inventario[codigo] = {'nombre': nombre, 'precio': precio}

# Definimos una función para quitar suministros del inventario
def quitar_suministros(codigo):
    # Verificamos si el código del suministro está en el diccionario inventario
    if codigo in inventario:
        # Si está, lo eliminamos del diccionario y devolvemos True para indicar que se quitó correctamente
        inventario.pop(codigo)
        return True
    # Si no está, devolvemos False para indicar que no se encontró el suministro
    return False

# Definimos una función para ordenar los suministros en el inventario
def ordenar_suministros(criterio):
    # Convertimos el diccionario inventario en una lista de tuplas para poder ordenarla
    items = list(inventario.items())

    # Definimos una función interna para ordenar la lista de tuplas utilizando el algoritmo de ordenamiento por mezcla (merge sort)
    def merge_sort(items, key):
        # Verificamos si la lista tiene más de un elemento
        if len(items) > 1:
            # Si tiene más de un elemento, la dividimos en dos mitades
            mid = len(items) // 2
            left_half = items[:mid]
            right_half = items[mid:]

            # Ordenamos cada mitad recursivamente llamando a la función merge_sort
            merge_sort(left_half, key)
            merge_sort(right_half, key)

            # Combinamos las dos mitades ordenadas en una sola lista ordenada
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if key(left_half[i]) < key(right_half[j]):
                    items[k] = left_half[i]
                    i += 1
                else:
                    items[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                items[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                items[k] = right_half[j]
                j += 1
                k += 1

    # Ordenamos la lista de tuplas según el criterio especificado utilizando la función merge_sort
    if criterio == 'nombre':
        merge_sort(items, key=lambda item: item[1]['nombre'])
    elif criterio == 'codigo':
        merge_sort(items, key=lambda item: item[0])

    # Devolvemos la lista de tuplas ordenada
    return items

# Definimos una función para buscar un producto en el inventario por código o por nombre
def buscar_producto(busqueda):
    # Iteramos sobre los elementos del diccionario inventario
    for codigo, producto in inventario.items():
        # Verificamos si el código o el nombre del producto coincide con la búsqueda
        if codigo == busqueda or producto['nombre'] == busqueda:
            # Si coincide, devolvemos el código del producto
            return codigo
    # Si no encontramos ningún producto que coincida con la búsqueda, devolvemos None
    return None

# Definimos una variable global para representar el saldo de la cuenta bancaria y la inicializamos con un valor de 1000
saldo_cuenta = 1000

# Definimos una función para cobrar productos a los clientes
def cobro_productos(lista_productos):
    # Inicializamos variables para almacenar el total a pagar y el ticket con los productos y sus precios
    total = 0
    ticket = []
    # Iteramos sobre la lista de códigos de productos que recibimos como argumento
    for busqueda in lista_productos:
        # Buscamos el código del producto en el inventario utilizando la función buscar_producto
        codigo = buscar_producto(busqueda)
        # Si encontramos el producto, sumamos su precio al total y agregamos su información al ticket
        if codigo:
            total += inventario[codigo]['precio']
            ticket.append(f"{codigo} - {inventario[codigo]['nombre']} - ${inventario[codigo]['precio']}")
    # Devolvemos el ticket y el total a pagar
    return ticket, total

# Definimos una función para registrar las quejas de los clientes
def atencion_clientes(codigo_producto, mensaje):
    # Agregamos la queja del cliente a la lista de clientes
    global clientes
    clientes.append({'codigo_producto': codigo_producto, 'mensaje': mensaje})

# Definimos una función para dar de alta a un trabajador
def alta_trabajador(codigo, nombre, apellido, puesto):
    # Agregamos el trabajador al diccionario de trabajadores con el código como clave y un diccionario con su información como valor
    trabajadores[codigo] = {'nombre': nombre, 'apellido': apellido, 'puesto': puesto}

# Definimos una función para dar de baja a un trabajador
def baja_trabajador(codigo):
    # Verificamos si el código del trabajador está en el diccionario de trabajadores
    if codigo in trabajadores:
        # Si está, lo eliminamos del diccionario y devolvemos True para indicar que se dio de baja correctamente
        trabajadores.pop(codigo)
        return True
    # Si no está, devolvemos False para indicar que no se encontró al trabajador
    return False

# Definimos una función para cambiar el puesto de un trabajador
def cambio_puesto(codigo, nuevo_puesto):
    # Verificamos si el código del trabajador está en el diccionario de trabajadores
    if codigo in trabajadores:
        # Si está, actualizamos su puesto en el diccionario y devolvemos True para indicar que se cambió correctamente
        trabajadores[codigo]['puesto'] = nuevo_puesto
        return True
    else:
        # Si no está, devolvemos False para indicar que no se encontró al trabajador
        return False

# Definimos una ruta para la URL raíz (/) de la aplicación web
@app.route('/')
def menu():
    # Renderizamos la plantilla menu.html y la devolvemos como respuesta al usuario
    return render_template('menu.html')

# Definimos una ruta para la URL /inventario de la aplicación web
@app.route('/inventario')
def menu_inventario():
    # Renderizamos la plantilla menu_inventario.html y la devolvemos como respuesta al usuario
    return render_template('menu_inventario.html')

# Definimos una ruta para la URL /inventario/mostrar de la aplicación web
@app.route('/inventario/mostrar')
def mostrar_inventario():
    # Renderizamos la plantilla mostrar_inventario.html y le pasamos el diccionario inventario como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
    return render_template('mostrar_inventario.html', inventario=inventario)

# Definimos una ruta para la URL /inventario/agregar de la aplicación web que acepta métodos GET y POST
@app.route('/inventario/agregar', methods=['GET', 'POST'])
def agregar_suministros_view():
    # Verificamos si el método de la solicitud es POST (es decir, si el usuario envió un formulario)
    if request.method == 'POST':
        # Si el método es POST, tomamos los datos del suministro del formulario enviado por el usuario
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        # Llamamos a la función agregar_suministros para agregar el suministro al inventario
        agregar_suministros(codigo, nombre, precio)
        # Renderizamos la plantilla agregar_suministro.html y le pasamos un mensaje y el diccionario inventario como variables. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
        return render_template('agregar_suministro.html', mensaje=f'Producto agregado: {codigo} - {nombre} - ${precio}', inventario=inventario)
    else:
        # Si el método no es POST (es decir, si el usuario está accediendo a la página por primera vez), simplemente renderizamos la plantilla agregar_suministro.html y le pasamos el diccionario inventario como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
        return render_template('agregar_suministro.html', inventario=inventario)
# Definimos una ruta para la URL /inventario/quitar de la aplicación web que acepta métodos GET y POST
@app.route('/inventario/quitar', methods=['GET', 'POST'])
def quitar_suministros_view():
    # Verificamos si el método de la solicitud es POST (es decir, si el usuario envió un formulario)
    if request.method == 'POST':
        # Si el método es POST, tomamos el código del suministro del formulario enviado por el usuario
        codigo = request.form['codigo']
        # Llamamos a la función quitar_suministros para quitar el suministro del inventario
        if quitar_suministros(codigo):
            # Si el suministro se quitó correctamente, renderizamos la plantilla quitar_suministros.html y le pasamos un mensaje como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            return render_template('quitar_suministros.html', mensaje='Suministro quitado')
        else:
            # Si el suministro no se encontró, renderizamos la plantilla quitar_suministros.html y le pasamos un mensaje de error como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            return render_template('quitar_suministros.html', mensaje='Producto no encontrado. Favor de ingresar el código correcto')
    else:
        # Si el método no es POST (es decir, si el usuario está accediendo a la página por primera vez), simplemente renderizamos la plantilla quitar_suministros.html y la devolvemos como respuesta al usuario.
        return render_template('quitar_suministros.html')

# Definimos una ruta para la URL /inventario/ordenar de la aplicación web que acepta métodos GET y POST
@app.route('/inventario/ordenar', methods=['GET', 'POST'])
def ordenar_suministros_view():
    # Verificamos si el método de la solicitud es POST (es decir, si el usuario envió un formulario)
    if request.method == 'POST':
        # Si el método es POST, tomamos el criterio de ordenamiento del formulario enviado por el usuario
        criterio = request.form['criterio']
        # Llamamos a la función ordenar_suministros para obtener una lista de suministros ordenados según el criterio especificado
        ordenados = ordenar_suministros(criterio)
        # Renderizamos la plantilla ordenar_suministros.html y le pasamos la lista de suministros ordenados como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
        return render_template('ordenar_suministros.html', ordenados=ordenados)
    else:
        # Si el método no es POST (es decir, si el usuario está accediendo a la página por primera vez), simplemente renderizamos la plantilla ordenar_suministros.html y la devolvemos como respuesta al usuario.
        return render_template('ordenar_suministros.html')

# Definimos una ruta para la URL /clientes de la aplicación web
@app.route('/clientes')
def menu_clientes():
    # Renderizamos la plantilla menu_clientes.html y la devolvemos como respuesta al usuario
    return render_template('menu_clientes.html')

# Definimos una ruta para la URL /clientes/cobrar de la aplicación web que acepta métodos GET y POST
@app.route('/clientes/cobrar', methods=['GET', 'POST'])
def cobrar_productos():
    global saldo_cuenta
    # Verificamos si el método de la solicitud es POST (es decir, si el usuario envió un formulario)
    if request.method == 'POST':
        # Si el método es POST, verificamos si el formulario enviado por el usuario contiene un campo llamado cuenta_bancaria
        if 'cuenta_bancaria' in request.form:
            # Si contiene un campo llamado cuenta_bancaria, tomamos el ticket y el total del formulario enviado por el usuario
            cuenta_bancaria = request.form['cuenta_bancaria']
            ticket = request.form.getlist('ticket')
            total = float(request.form['total'])
            # Renderizamos la plantilla pago_realizado.html y le pasamos el ticket, el total y otras variables como variables. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            return render_template('pago_realizado.html', ticket=ticket, total=total, inventario=inventario, saldo_cuenta=saldo_cuenta)
        else:
            # Si no contiene un campo llamado cuenta_bancaria, tomamos el tipo y los productos del formulario enviado por el usuario
            tipo = request.form['tipo']
            productos = request.form['productos']
            # Separamos los productos por comas para obtener una lista de códigos o nombres de productos
            lista_productos = productos.split(',')
            # Verificamos si el tipo es codigo o nombre
            if tipo == 'codigo':
                # Si el tipo es codigo, verificamos si los códigos ingresados son válidos
                for codigo in lista_productos:
                    if codigo not in inventario:
                        # Si encontramos un código inválido, renderizamos la plantilla cobrar_productos.html y le pasamos un mensaje de error como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
                        return render_template('cobrar_productos.html', error='Producto no encontrado. Favor de intentar nuevamente.', inventario=inventario, saldo_cuenta=saldo_cuenta)
                # Si todos los códigos son válidos, llamamos a la función cobro_productos para obtener un ticket y un total a pagar
                ticket, total = cobro_productos(lista_productos)
            else:
                # Si el tipo es nombre, convertimos los nombres ingresados a códigos
                codigos_productos = []
                for nombre in lista_productos:
                    codigo_encontrado = False
                    for codigo, producto in inventario.items():
                        if producto['nombre'] == nombre:
                            codigos_productos.append(codigo)
                            codigo_encontrado = True
                            break
                    if not codigo_encontrado:
                        # Si encontramos un nombre inválido, renderizamos la plantilla cobrar_productos.html y le pasamos un mensaje de error como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
                        return render_template('cobrar_productos.html', error='Producto no encontrado. Favor de intentar nuevamente.', inventario=inventario, saldo_cuenta=saldo_cuenta)
                # Si todos los nombres son válidos, llamamos a la función cobro_productos para obtener un ticket y un total a pagar
                ticket, total = cobro_productos(codigos_productos)
            # Actualizamos el saldo de la cuenta y renderizamos la plantilla cobrar_productos.html y le pasamos el ticket, el total y otras variables como variables. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            saldo_cuenta -= total
            return render_template('cobrar_productos.html', ticket=ticket, total=total, inventario=inventario, saldo_cuenta=saldo_cuenta)
    else:
        # Si el método no es POST (es decir, si el usuario está accediendo a la página por primera vez), simplemente renderizamos la plantilla cobrar_productos.html y le pasamos el diccionario inventario y otras variables como variables. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
        return render_template('cobrar_productos.html', inventario=inventario, saldo_cuenta=saldo_cuenta)

# Definimos una ruta para la URL /atender_cliente de la aplicación web
@app.route('/atender_cliente')
def atender_cliente():
    # Tomamos el código del producto y el mensaje del cliente de los argumentos de la URL
    codigo_producto = request.args.get('codigo_producto')
    mensaje = request.args.get('mensaje')
    
    # Verificamos si se especificaron el código del producto y el mensaje del cliente en los argumentos de la URL
    if codigo_producto and mensaje:
        # Si se especificaron, buscamos el producto en el inventario utilizando la función buscar_producto
        if buscar_producto(codigo_producto):
            # Si encontramos el producto, llamamos a la función atencion_clientes para registrar la queja del cliente
            atencion_clientes(codigo_producto, mensaje)
            # Renderizamos la plantilla atender_cliente.html y le pasamos un mensaje como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            return render_template('atender_cliente.html', mensaje='Queja registrada')
        else:
            # Si no encontramos el producto, renderizamos la plantilla atender_cliente.html y le pasamos un mensaje de error como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            return render_template('atender_cliente.html', mensaje='Producto no encontrado. Favor de ingresar un producto válido.')
    
    # Si no se especificaron el código del producto y el mensaje del cliente en los argumentos de la URL, simplemente renderizamos la plantilla atender_cliente.html y la devolvemos como respuesta al usuario.
    return render_template ('atender_cliente.html')

# Definimos una ruta para la URL /personal de la aplicación web
@app.route('/personal')
def menu_personal():
    # Renderizamos la plantilla menu_personal.html y la devolvemos como respuesta al usuario
    return render_template('menu_personal.html')

# Definimos una ruta para la URL /personal/alta de la aplicación web que acepta métodos GET y POST
@app.route('/personal/alta', methods=['GET', 'POST'])
def alta_trabajador_view():
    # Verificamos si el método de la solicitud es POST (es decir, si el usuario envió un formulario)
    if request.method == 'POST':
        # Si el método es POST, tomamos los datos del trabajador del formulario enviado por el usuario
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        puesto = request.form['puesto']
        # Llamamos a la función alta_trabajador para dar de alta al trabajador en el sistema
        alta_trabajador(codigo, nombre, apellido, puesto)
        # Renderizamos la plantilla alta_trabajador.html y le pasamos un mensaje como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
        return render_template('alta_trabajador.html', mensaje=f'Trabajador dado de alta: {codigo} - {nombre} {apellido} - {puesto}')
    else:
        # Si el método no es POST (es decir, si el usuario está accediendo a la página por primera vez), simplemente renderizamos la plantilla alta_trabajador.html y la devolvemos como respuesta al usuario.
        return render_template('alta_trabajador.html')

# Definimos una ruta para la URL /personal/baja de la aplicación web que acepta métodos GET y POST
@app.route('/personal/baja', methods=['GET', 'POST'])
def baja_trabajador_view():
    # Verificamos si el método de la solicitud es POST (es decir, si el usuario envió un formulario)
    if request.method == 'POST':
        # Si el método es POST, tomamos el código del trabajador del formulario enviado por el usuario
        codigo = request.form['codigo']
        # Llamamos a la función baja_trabajador para dar de baja al trabajador en el sistema
        if baja_trabajador(codigo):
            # Si el trabajador se dio de baja correctamente, renderizamos la plantilla baja_trabajador.html y le pasamos un mensaje como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            return render_template('baja_trabajador.html', mensaje='Trabajador dado de baja')
        else:
            # Si no se encontró al trabajador, renderizamos la plantilla baja_trabajador.html y le pasamos un mensaje de error como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            return render_template('baja_trabajador.html', mensaje='Trabajador no encontrado. Favor de ingresar un código válido.')
    else:
        # Si el método no es POST (es decir, si el usuario está accediendo a la página por primera vez), simplemente renderizamos la plantilla baja_trabajador.html y la devolvemos como respuesta al usuario.
        return render_template('baja_trabajador.html')

# Definimos una ruta para la URL /personal/cambio_puesto de la aplicación web que acepta métodos GET y POST
@app.route('/personal/cambio_puesto', methods=['GET', 'POST'])
def cambio_puesto_view():
    # Verificamos si el método de la solicitud es POST (es decir, si el usuario envió un formulario)
    if request.method == 'POST':
        # Si el método es POST, tomamos el código y el nuevo puesto del trabajador del formulario enviado por el usuario
        codigo = request.form['codigo']
        nuevo_puesto = request.form['nuevo_puesto']
        # Verificamos si el código del trabajador está en el diccionario de trabajadores
        if codigo in trabajadores:
            # Si está, actualizamos su puesto en el diccionario y renderizamos la plantilla cambio_puesto.html y le pasamos un mensaje como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            cambio_puesto(codigo, nuevo_puesto)
            return render_template('cambio_puesto.html', mensaje=f'Puesto cambiado: {codigo} - {trabajadores[codigo]["nombre"]} {trabajadores[codigo]["apellido"]} - {nuevo_puesto}')
        else:
            # Si no está, renderizamos la plantilla cambio_puesto.html y le pasamos un mensaje de error como variable. Luego, devolvemos la plantilla renderizada como respuesta al usuario.
            return render_template('cambio_puesto.html', mensaje='Trabajador no encontrado. Favor de ingresar un código válido.')
    else:
        # Si el método no es POST (es decir, si el usuario está accediendo a la página por primera vez), simplemente renderizamos la plantilla cambio_puesto.html y la devolvemos como respuesta al usuario.
        return render_template('cambio_puesto.html')

# Verificamos si el script se está ejecutando directamente (en lugar de ser importado como un módulo)
if __name__ == '__main__':
    # Si el script se está ejecutando directamente, ejecutamos la aplicación Flask en modo de depuración en el puerto 5000
    app.run(debug=True, port=5000)