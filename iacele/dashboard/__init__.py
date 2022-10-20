# Se importan las librerías necesarias para este blueprint (sub-app).
from flask import Blueprint


# Se instancía la clase Blueprint para generar el objeto 'dashboard', que es
# una de las sub-app del proyecto 'iacele'.
dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


#Se importa la 'vista' (url y end-points) de este blueprint.
from iacele.dashboard import views