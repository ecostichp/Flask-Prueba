# Se importan las librerías necesarias para este blueprint (sub-app).
from flask import Blueprint


# Se instancía la clase Blueprint para generar el objeto 'cotizaciones_prueba', que es
# una de las sub-app del proyecto 'iacele'.
cotizaciones_prueba = Blueprint('cotizaciones_prueba', __name__, url_prefix='/cotizaciones_prueba')


#Se importa la 'vista' (url y end-points) de este blueprint.
from iacele.cotizaciones_prueba import views