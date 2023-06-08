from flask import Flask, request, render_template

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

def atencion_clientes(codigo_producto, mensaje):
    global clientes
    clientes.append({'codigo_producto': codigo_producto, 'mensaje': mensaje})

def alta_trabajador(codigo, nombre, apellido, puesto):
    trabajadores[codigo] = {'nombre': nombre, 'apellido': apellido, 'puesto': puesto}

def baja_trabajador(codigo):
    if codigo in trabajadores:
        trabajadores.pop(codigo)
        print(f"El trabajador con código {codigo} ha sido dado de baja.")
    else:
        print(f"No se encontró un trabajador con código {codigo}.")

def cambio_puesto(codigo, nuevo_puesto):
    if codigo in trabajadores:
        trabajadores[codigo]['puesto'] = nuevo_puesto
        return True
    else:
        print(f"No se encontró un trabajador con código {codigo}.")
        return False

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
    if request.method == 'POST':
        codigo = request.form['codigo']
        quitar_suministros(codigo)
        return render_template('quitar_suministro.html', success=True)
    else:
        return render_template('quitar_suministro.html')

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

@app.route('/personal/cambio_puesto', methods=['GET', 'POST'])
def cambio_puesto_view():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nuevo_puesto = request.form['nuevo_puesto']
        cambio_puesto(codigo, nuevo_puesto)
        return render_template('cambio_puesto.html', success=True)
    else:
        return render_template('cambio_puesto.html')

if __name__ == '__main__':
    app.run()