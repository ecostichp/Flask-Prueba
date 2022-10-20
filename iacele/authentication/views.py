# Se importan las librerías necesarias para este blueprint (sub-app).
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user, current_user



#Se importa el blueprint desde esta sub-app (Se genera una dependencia circular)
from iacele.authentication import authentication


# Se importa la función 'user_loader' que tiene el 'callback' de la librería 
# 'login_manager'. Esto es neceario para acceder a 'current_user' en esta 'vista'.
from iacele.authentication.login import user_loader


# Se importa la clase User desde el 'modelo' de esta sub-app, para que la lógica
# de esta 'vista' pueda instanciar nuevos objetos (nuevos registros en la tabla
# User de la base de datos)
from iacele.authentication.models import Usuarios

# Se importan los formularios de esta sub-app. La 'vista', por medio de los end-points,
# mandará estos formularios dentro de los templates para recoger información del
# usuario y así relizar la lógica necesaria.
from iacele.authentication.forms import Formulario_iniciar_sesion, Formulario_registrar_usuario



# Se contruyen todas las rutas de esta sub-app y debajo de ellas el
# end-point (función que contine la lógica de la ruta)

# Este end-point es la URL 'raiz' del proyecto. Se trabaja el logueo del usuario.
@authentication.route("/", methods=['GET', 'POST'])
def iniciar_sesion():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    else:
        form = Formulario_iniciar_sesion()
        if form.validate_on_submit() and request.method == 'POST':
            
            usuario_en_validacion = request.form['usuario']
            contraseña_en_validacion = request.form['contraseña']
            
            usuario_validado = Usuarios.get_by_user(usuario_en_validacion)
            if usuario_validado is not None and usuario_validado.verify_password(contraseña_en_validacion):
                login_user(usuario_validado)
                return redirect(url_for('dashboard.index'))
            flash('Usuario o contraseña inválidos.', 'danger')

        return render_template ('authentication/iniciar_sesion.html', name=iniciar_sesion,form=form)


# Este end-point trabaja el registro del usuario nuevo a nuestra tabla Users.
@authentication.route("/registrar_usuario", methods=['GET', 'POST'])
def registrar_usuario():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    else:
        form = Formulario_registrar_usuario()
        if form.validate_on_submit() and request.method == 'POST':
            usuario = request.form['usuario']
            nombre_1ro = request.form['nombre_1ro']
            nombre_2do = None if request.form['nombre_2do'] == '' else request.form['nombre_2do']
            apellido_paterno = request.form['apellido_paterno']
            apellido_materno = request.form['apellido_materno']
            almacen = request.form['almacen']
            foto = request.form['foto']
            contraseña = request.form['contraseña']
           
            usuario = Usuarios(usuario=usuario, nombre_1ro=nombre_1ro, nombre_2do=nombre_2do, apellido_paterno=apellido_paterno,
                     apellido_materno=apellido_materno, almacen=almacen, foto=foto)
            
            usuario.set_password(contraseña)
            usuario.save()
            return redirect(url_for('authentication.iniciar_sesion'))
        return render_template ('authentication/registrar_usuario.html', name=registrar_usuario,form=form)


# Este end-ponit trabaja el cambio de contraseña del usuario, cuando este no lo recuerda.
@authentication.route("/cambiar_contraseña", methods=['GET', 'POST'])
def cambiar_contraseña():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    else:
        form = 'Falta por ser creado'
        return render_template ('authentication/cambiar_contraseña.html', name=cambiar_contraseña,form=form)


# Este end-point trabaja el logout del usuario.
@authentication.route("/sign_out")
@login_required
def sign_out():
    logout_user()
    return redirect(url_for("authentication.iniciar_sesion"))