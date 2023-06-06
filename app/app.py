from flask import Flask, render_template, request
app = Flask(__name__, template_folder='bin')

inventario = {}
clientes = []
trabajadores = {}

def agregar_suministros(codigo, nombre):
    inventario[codigo] = nombre

def quitar_suministros(codigo):
    if codigo in inventario:
        inventario[codigo] = None

def ordenar_por_nombre(item):
    return item[1]

def ordenar_por_codigo(item):
    return item[0]

def ordenar_suministros(criterio):
    items = []
    
    for k in inventario:
        v = inventario[k]
        items += [(k, v)]
    
    if criterio == 'nombre':
        items.sort(key=ordenar_por_nombre)
    elif criterio == 'codigo':
        items.sort(key=ordenar_por_codigo)
    
    result = []
    
    for k, v in items:
        result += [(k, v)]
    
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventario')
def ver_inventario():
    return render_template('inventario.html', inventario=inventario)

@app.route('/clientes')
def ver_clientes():
    return render_template('clientes.html', clientes=clientes)

@app.route('/trabajadores')
def ver_trabajadores():
    return render_template('trabajadores.html', trabajadores=trabajadores)

@app.route('/trabajadores/alta', methods=['GET', 'POST'])
def alta_trabajador():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        puesto = request.form['puesto']
        
        trabajadores[codigo] = {'nombre': nombre, 'apellido': apellido, 'puesto': puesto}
        
        return render_template('alta_trabajador.html', alta=True)
    else:
                return render_template('alta_trabajador.html', alta=False)

@app.route('/trabajadores/baja', methods=['GET', 'POST'])
def baja_trabajador():
    if request.method == 'POST':
        codigo = request.form['codigo']
        
        if codigo in trabajadores:
            trabajadores[codigo] = None
        
        return render_template('baja_trabajador.html', baja=True)
    else:
        return render_template('baja_trabajador.html', baja=False)

@app.route('/trabajadores/cambio', methods=['GET', 'POST'])
def cambio_trabajador():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nuevo_puesto = request.form['nuevo_puesto']
        
        trabajadores[codigo]['puesto'] = nuevo_puesto
        
        return render_template('cambio_trabajador.html', cambio=True)
    else:
        return render_template('cambio_trabajador.html', cambio=False)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/inventario/menu')
def menu_inventario():
    return render_template('menu_inventario.html')

@app.route('/inventario/agregar', methods=['GET', 'POST'])
def agregar_inventario():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        agregar_suministros(codigo, nombre)
        return render_template('agregar_inventario.html', agregado=True)
    else:
        return render_template('agregar_inventario.html', agregado=False)

@app.route('/inventario/quitar', methods=['GET', 'POST'])
def quitar_inventario():
    if request.method == 'POST':
        codigo = request.form['codigo']
        quitar_suministros(codigo)
        return render_template('quitar_inventario.html', quitado=True)
    else:
        return render_template('quitar_inventario.html', quitado=False)

@app.route('/inventario/ordenar', methods=['GET', 'POST'])
def ordenar_inventario():
    if request.method == 'POST':
        criterio = request.form['criterio']
        ordenados = ordenar_suministros(criterio)
        return render_template('ordenar_inventario.html', ordenados=ordenados)
    else:
        return render_template('ordenar_inventario.html')

@app.route('/personal/menu')
def menu_personal():
    return render_template('menu_personal.html')

@app.route('/personal/alta', methods=['GET', 'POST'])
def alta_personal():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        puesto = request.form['puesto']
        
        trabajadores[codigo] = {'nombre': nombre, 'apellido': apellido, 'puesto': puesto}
        
        return render_template('alta_personal.html', alta=True)
    else:
        return render_template('alta_personal.html', alta=False)

@app.route('/personal/baja', methods=['GET', 'POST'])
def baja_personal():
    if request.method == 'POST':
        codigo = request.form['codigo']
        
        if codigo in trabajadores:
            trabajadores[codigo] = None
        
        return render_template('baja_personal.html', baja=True)
    else:
        return render_template('baja_personal.html', baja=False)

@app.route('/personal/cambio', methods=['GET', 'POST'])
def cambio_personal():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nuevo_puesto = request.form['nuevo_puesto']
        
        trabajadores[codigo]['puesto'] = nuevo_puesto
        
        return render_template('cambio_personal.html', cambio=True)
    else:
        return render_template('cambio_personal.html', cambio=False)

@app.route('/clientes/menu')
def menu_clientes():
    return render_template('menu_clientes.html')

@app.route('/clientes/cobro', methods=['GET', 'POST'])
def cobro_clientes():
    if request.method == 'POST':
        lista_productos = request.form.getlist('productos')
        
        total = cobro_productos(lista_productos)
        
        return render_template('cobro_clientes.html', total=total)
    else:
        return render_template('cobro_clientes.html')

@app.route('/clientes/atender', methods=['GET', 'POST'])
def atender_clientes():
    if request.method == 'POST':
        codigo_producto = request.form['codigo_producto']
        mensaje = request.form['mensaje']
        
        global clientes
        clientes_nuevos = []
        
        for cliente in clientes:
            clientes_nuevos += [cliente]
            
            clientes_nuevos += [{'codigo_producto': codigo_producto, 'mensaje': mensaje}]
        
        clientes = clientes_nuevos
        
        return render_template('atender_clientes.html', atendido=True)
    else:
        return render_template('atender_clientes.html', atendido=False)

if __name__ == '__main__':
    app.run()