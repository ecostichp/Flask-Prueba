# Se importan las librerías necesarias.
from flask_login import LoginManager
from flask import current_app
from iacele.authentication.models import Usuarios



# Se instancía el objeto 'login_manager'.
login_manager = LoginManager(current_app)



# Este es un 'callback' necesario para la librería 'Flask_Login. El decorador usa
# el objeto 'login_manager' instanciado en la línea anterior. El objetivo es 
# buscar cada usuario en las 'sesiones abiertas guardadas de la librería'.
# Si el usuario se encuentra, devuelve el objeto del usuario. Si no se encuentra,
# remueve al usuario de las sesiones abierta y devuelve un 'None'.
@login_manager.user_loader
def user_loader(id):
    return Usuarios.get_by_id(id)



# Cuando en los end-point de los blueprint (sub-apps) se antepone el decorador
# '@login_required', los usuarios no logueados no pueden ingresar a la URL (ruta).
# Se utiliza el siguiente método del objeto 'login_manager' para re-dirigir al usuario
# al end-point necesario para logearse.
login_manager.login_view = 'authentication.iniciar_sesion'

# Mensaje por defecto que envía Flask-Flash al ingresar a una ruta URL que tiene
# '@login_required' y el usuario no está sesionado.
login_manager.login_message = 'Por favor, inicia sesión'

# Categoría del mensaje por defecto que envía Flask-Flash al ingresar a una ruta URL
# que tiene '@login_required' y el usuario no está sesionado.
login_manager.login_message_category = "default"