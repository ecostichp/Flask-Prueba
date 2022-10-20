# Se importan las librerías necesarias para la 'vista' de este blueprint
from flask import render_template
from flask_login import login_required



#Se importa el blueprint desde esta sub-app (Se genera una dependencia circular)
from iacele.dashboard import dashboard



# Se contruyen todas las rutas de esta sub-app y debajo de ellas el
# end-point (función que contine la lógica de la ruta)

# Este end-point trabaja el index de la sub-app, que es el index del proyecto.
@dashboard.route("/")
@login_required
def index():
    return render_template('dashboard/index.html')