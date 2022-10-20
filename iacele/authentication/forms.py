# Se importan las librerías necesarias para los formularios de este blueprint (sub-app).
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField, IntegerField



# Este formulario se usa en el template 'user_manager/iniciar_sesion.html'. La finalidad
# es que la 'vista' procese lógica con ellos para logear al usuario.
class Formulario_iniciar_sesion (FlaskForm):
    usuario = StringField ('Usuario')
    contraseña = PasswordField ('Contraseña')
    recuerdame = BooleanField ('Recordarme')
    enviar = SubmitField ('Enviar')


# Este formulario se usa en el template 'user_manager/registrar_usuario.html'. La finalidad
# es que la 'vista' procese lógica con ellos y utilice al 'modelo' para registrar nuevos
# usuarios en la tabla Users de la base de datos.
class Formulario_registrar_usuario (FlaskForm):  
    usuario = StringField(render_kw={"placeholder" : "Usuario"})
    nombre_1ro = StringField(render_kw={"placeholder" : "Primer Nombre"})
    nombre_2do = StringField(render_kw={"placeholder" : "Segundo Nombre"})
    apellido_paterno = StringField(render_kw={"placeholder" : "Apellido Paterno"})
    apellido_materno = StringField(render_kw={"placeholder" : "Apellido Materno"})
    almacen = IntegerField (render_kw={"placeholder" : "almacen"})
    foto = StringField(render_kw={"placeholder" : "Foto"})
    contraseña = PasswordField(render_kw={"placeholder" : "Contraseña"})
    guardar = SubmitField(render_kw={"placeholder" : "Guardar"})