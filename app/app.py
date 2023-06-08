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
    return render_template('menu.html')

@app.route('/inventario')
def menu_inventario():
    return render_template('menu_inventario.html')

@app.route('/agregar_suministros', methods=['POST'])
def agregar_suministros_route():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    
    agregar_suministros(codigo, nombre, precio)
    
    return f'Suministro agregado: {codigo} - {nombre} - ${precio}'

@app.route('/quitar_suministros', methods=['POST'])
def quitar_suministros_route():
    busqueda = request.form['busqueda']
    
    if quitar_suministros(busqueda):
        return 'Suministro quitado'
    else:
        return 'Suministro no encontrado'

@app.route('/ordenar_suministros', methods=['POST'])
def ordenar_suministros_route():
    criterio = request.form['criterio']
    
    ordenados = ordenar_suministros(criterio)
    
    resultado = ''
    
    for codigo, producto in ordenados:
        resultado += f'{codigo} - {producto["nombre"]} - ${producto["precio"]}<br>'
    
    return resultado

@app.route('/clientes')
def menu_clientes():
        return render_template('menu_clientes.html')

@app.route('/cobro_productos', methods=['POST'])
def cobro_productos_route():
    lista_productos = request.form.getlist('productos')
    
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
    
    resultado = "Ticket de pago:<br>"
    resultado += "<br>".join(ticket)
    resultado += f"<br><br>Total: ${total}<br>"
    
    if total <= saldo_cuenta:
        cuenta_bancaria = request.form['cuenta_bancaria']
        saldo_cuenta -= total
        
        resultado += f"<br>Se ha realizado el cobro a la cuenta {cuenta_bancaria}<br>"
        resultado += f"Saldo restante en la cuenta: ${saldo_cuenta}<br>"
    else:
        resultado += "No hay suficiente saldo en la cuenta para realizar el pago<br>"
    
    return resultado

@app.route('/atencion_clientes', methods=['POST'])
def atencion_clientes_route():
    codigo_producto = request.form['codigo_producto']
    mensaje = request.form['mensaje']
    
    atencion_clientes(codigo_producto, mensaje)
    
    return 'Queja registrada'

@app.route('/personal')
def menu_personal():
    return render_template('menu_personal.html')

@app.route('/alta_trabajador', methods=['POST'])
def alta_trabajador_route():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    puesto = request.form['puesto']

    alta_trabajador(codigo, nombre, apellido, puesto)

    return 'Trabajador dado de alta'

@app.route('/baja_trabajador', methods=['POST'])
def baja_trabajador_route():
    codigo = request.form['codigo']

    baja_trabajador(codigo)

    return 'Trabajador dado de baja'

@app.route('/cambio_puesto', methods=['POST'])
def cambio_puesto_route():
    codigo = request.form['codigo']
    nuevo_puesto = request.form['nuevo_puesto']

    cambio_realizado = cambio_puesto(codigo, nuevo_puesto)

    if cambio_realizado:
        return 'Cambio realizado'
    
if __name__ == '__main__':
    app.run()