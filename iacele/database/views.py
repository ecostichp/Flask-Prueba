# Se importan las librerías necesarias para la 'vista' de este blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user


#Se importa el blueprint desde esta sub-app (Se genera una dependencia circular)
from iacele.database import database


from iacele.database.forms import Formulario_Inser_Bulk_Data
from iacele.database.bulk_insert_db import bulk_data


from iacele.authentication.models import Usuarios
from iacele.cotizaciones_prueba.models import Productos, Proveedores, Clientes



# Se contruyen todas las rutas de esta sub-app y debajo de ellas el
# end-point (función que contine la lógica de la ruta)

# Este end-point trabaja el index de la sub-app, que es el index del proyecto.
@database.route("/", methods=['GET', 'POST'])
@login_required
def insert_bulk_data():
    form = Formulario_Inser_Bulk_Data()
    usuarios = bulk_data('usuarios')

    if form.validate_on_submit() and request.method == 'POST':
        for el in usuarios:
            usuario = el['usuario']
            nombre_1ro = el['nombre_1ro']
            nombre_2do = el['nombre_2do']
            apellido_paterno = el['apellido_paterno']
            apellido_materno = el['apellido_materno']
            almacen = el['almacen']
            foto = el['foto']
            contraseña = el['contraseña']

            usuario = Usuarios(usuario=usuario, nombre_1ro=nombre_1ro, nombre_2do=nombre_2do, apellido_paterno=apellido_paterno,
                     apellido_materno=apellido_materno, almacen=almacen, foto=foto)
            usuario.set_password(contraseña)
            usuario.save()
        
        print('\n>>>Los usuarios se registraron con éxito en la base de datos.\n')

    return render_template('database/insert_bulk_data.html', name=insert_bulk_data, form=form, usuarios=usuarios)