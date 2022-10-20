# Se importan las librerías necesarias para este blueprint (sub-app).
from flask import Blueprint


# Se instancía la clase Blueprint para generar el objeto 'database', que es
# una de las sub-app del proyecto 'iacele'.
database = Blueprint('database', __name__, url_prefix='/database')


#Se importa la 'vista' (url y end-points) de este blueprint.
from iacele.database import views