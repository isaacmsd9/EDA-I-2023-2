from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

inventario = {}
clientes = []
trabajadores = {}

def agregar_suministros(codigo, nombre, precio):
    inventario[codigo] = {'nombre': nombre, 'precio': precio}

def quitar_suministros(codigo):
    if codigo in inventario:
        inventario.pop(codigo)
        return True
    return False

def ordenar_suministros(criterio):
    items = list(inventario.items())
    if criterio == 'nombre':
        items.sort(key=lambda item: item[1]['nombre'])
    elif criterio == 'codigo':
        items.sort(key=lambda item: item[0])
    return items

def buscar_producto(busqueda):
    for codigo, producto in inventario.items():
        if codigo == busqueda or producto['nombre'] == busqueda:
            return codigo
    return None

saldo_cuenta = 1000

def cobro_productos(lista_productos):
    total = 0
    ticket = []
    for busqueda in lista_productos:
        codigo = buscar_producto(busqueda)
        if codigo:
            total += inventario[codigo]['precio']
            ticket.append(f"{codigo} - {inventario[codigo]['nombre']} - ${inventario[codigo]['precio']}")
    return ticket, total

def atencion_clientes(codigo_producto, mensaje):
    global clientes
    clientes.append({'codigo_producto': codigo_producto, 'mensaje': mensaje})

def alta_trabajador(codigo, nombre, apellido, puesto):
    trabajadores[codigo] = {'nombre': nombre, 'apellido': apellido, 'puesto': puesto}

def baja_trabajador(codigo):
    if codigo in trabajadores:
        trabajadores.pop(codigo)

def cambio_puesto(codigo, nuevo_puesto):
    if codigo in trabajadores:
        trabajadores[codigo]['puesto'] = nuevo_puesto
        return True
    else:
        return False

@app.route('/')
def menu():
    # Muestra el menú principal
    return render_template('menu.html')

@app.route('/inventario')
def menu_inventario():
    # Muestra el menú de administración de inventario
    return render_template('menu_inventario.html')

@app.route('/inventario/mostrar')
def mostrar_inventario():
    return render_template('mostrar_inventario.html', inventario=inventario)

@app.route('/inventario/agregar', methods=['GET', 'POST'])
def agregar_suministros_view():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        agregar_suministros(codigo, nombre, precio)
        return redirect(url_for('menu_inventario'))
    else:
        return render_template('agregar_suministro.html')

@app.route('/inventario/quitar', methods=['GET', 'POST'])
def quitar_suministros_view():
    if request.method == 'POST':
        codigo = request.form['codigo']
        if quitar_suministros(codigo):
            return render_template('quitar_suministros.html', mensaje='Suministro quitado')
        else:
            return render_template('quitar_suministros.html', mensaje='Producto no encontrado. Favor de ingresar el código correcto')
    else:
        return render_template('quitar_suministros.html')

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
    global saldo_cuenta
    if request.method == 'POST':
        if 'cuenta_bancaria' in request.form:
            cuenta_bancaria = request.form['cuenta_bancaria']
            ticket = request.form.getlist('ticket')
            total = float(request.form['total'])
            # Aquí puedes agregar código para procesar el pago utilizando la cuenta bancaria del usuario
            return render_template('pago_realizado.html', ticket=ticket, total=total, inventario=inventario, saldo_cuenta=saldo_cuenta)
        else:
            tipo = request.form['tipo']
            productos = request.form['productos']
            lista_productos = productos.split(',')
            if tipo == 'codigo':
                # Verificar si los códigos ingresados son válidos
                for codigo in lista_productos:
                    if codigo not in inventario:
                        return render_template('cobrar_productos.html', error='Producto no encontrado. Favor de intentar nuevamente.', inventario=inventario, saldo_cuenta=saldo_cuenta)
                ticket, total = cobro_productos(lista_productos)
            else:
                # Convertir los nombres ingresados a códigos
                codigos_productos = []
                for nombre in lista_productos:
                    codigo_encontrado = False
                    for codigo, producto in inventario.items():
                        if producto.nombre == nombre:
                            codigos_productos.append(codigo)
                            codigo_encontrado = True
                            break
                    if not codigo_encontrado:
                        return render_template('cobrar_productos.html', error='Producto no encontrado. Favor de intentar nuevamente.', inventario=inventario, saldo_cuenta=saldo_cuenta)
                ticket, total = cobro_productos(codigos_productos)
            saldo_cuenta -= total
            return render_template('cobrar_productos.html', ticket=ticket, total=total, inventario=inventario, saldo_cuenta=saldo_cuenta)
    else:
        return render_template('cobrar_productos.html', inventario=inventario, saldo_cuenta=saldo_cuenta)

@app.route('/clientes/atender', methods=['GET', 'POST'])
def atender_cliente():
    if request.method == 'POST':
        codigo = request.form['codigo']
        producto = inventario.get(codigo)
        if producto:
            if 'mensaje' in request.form:
                mensaje = request.form['mensaje']
                atencion_clientes(codigo, mensaje)
                return render_template('atender_cliente.html', producto=producto, mensaje='Gracias por su mensaje')
            else:
                return render_template('atender_cliente.html', producto=producto)
        else:
            return render_template('atender_cliente.html', error='Producto no encontrado. Favor de ingresar el código correcto')
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

@app.route('/personal/cambio_puesto', methods=['GET', 'POST'])
def cambio_puesto():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nuevo_puesto = request.form['nuevo_puesto']
        cambio_puesto(codigo, nuevo_puesto)
        return render_template('cambio_puesto.html', success=True)
    else:
        return render_template('cambio_puesto.html')

if __name__ == '__main__':
    app.run()