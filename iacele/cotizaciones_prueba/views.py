# Se importan las librerías necesarias para este blueprint (sub-app).
from flask import render_template
from flask_login import login_required



#Se importa el blueprint desde esta sub-app (Se genera una dependencia circular)
from iacele.cotizaciones_prueba import cotizaciones_prueba



# Se importan los formularios de esta sub-app. La 'vista', por medio de los end-points,
# mandará estos formularios dentro de los templates para recoger información del
# usuario y así relizar la lógica necesaria.
from iacele.cotizaciones_prueba.forms import Formulario_Cotizacion


# Se importa la clase User desde el 'modelo' de esta sub-app, para que la lógica
# de esta 'vista' pueda instanciar nuevos objetos (nuevos registros en la tabla
# User de la base de datos)
from iacele.cotizaciones_prueba.models import Productos, Clientes, Proveedores


# Esta lógica se va a reemplazar una vez utilizando modelos y db. Ahorita sólo se está
# entregando una lista vacía. Los templates tendrán problemas.

ver_cotizaciones = []
ver_clientes = []
ver_vendedores = []
ver_productos = []



# Se contruyen todas las rutas de esta sub-app y debajo de ellas el
# end-point (función que contine la lógica de la ruta)

# Este end-point...
@cotizaciones_prueba.route("/cotizaciones_expandidas")
@login_required
def cotizaciones_expandidas():
    context= {
        "cotizaciones" : ver_cotizaciones
    }
    return render_template('cotizaciones_prueba/cotizaciones_expandidas.html', name=cotizaciones_expandidas, **context)


@cotizaciones_prueba.route("/lista_cotizaciones")
@login_required
def lista_cotizaciones():
    context= {
        "cotizaciones" : ver_cotizaciones
    }
    return render_template('cotizaciones_prueba/lista_cotizaciones.html', name=lista_cotizaciones, **context)


@cotizaciones_prueba.route("/nueva_cotizacion", methods=['GET', 'POST'])
@login_required
def nueva_cotizacion():
    context = {
        'clientes' : ver_clientes,
        'vendedores' : ver_vendedores,
        'productos' : ver_productos,
        'form' : Formulario_Cotizacion()
    }
    return render_template('cotizaciones_prueba/nueva_cotizacion.html', name=nueva_cotizacion, **context)



@cotizaciones_prueba.route("/prueba")
@login_required
def prueba():
    context = {
        'clientes' : ver_clientes,
        'vendedores' : ver_vendedores,
        'productos' : ver_productos,
    }
    return render_template('cotizaciones_prueba/prueba.html', name=prueba, **context)