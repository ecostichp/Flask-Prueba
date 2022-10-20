# Se importan las librerías necesarias para este blueprint (sub-app).
from flask import Blueprint


# Se instancía la clase Blueprint para generar el objeto 'authentication', que es
# una de las sub-app del proyecto 'iacele'.
authentication = Blueprint('authentication', __name__)


#Se importa la 'vista' (url y end-points) de este blueprint.
from iacele.authentication import views