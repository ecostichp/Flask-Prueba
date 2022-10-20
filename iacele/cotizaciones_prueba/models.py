# Se importan las librerías necesarias para el modelo de este blueprint (sub-app).


# Se importa el objeto 'db' desde el proyecto. El 'modelo' utilizará este objeto
# para comunicarse, a través de SQLAlchemy, con el motor de base de datos que se
# configuró en las variables de ambiente de entorno.
from iacele import db



# Se genera la clase User. Con este modelo, se genera la tabla User en la base de
# datos del proyecto. En esta tabla se registran los datos generales de los usuarios
# del proyecto. Se usará para el módulo de RH, permisos dentro de esta app, etc.
class Productos(db.Model): 
    id = db.Column(db.INTEGER, primary_key=True)
    codigo = db.Column(db.VARCHAR(16), nullable=False, unique=True)
    descripcion = db.Column(db.VARCHAR(128), nullable=False)
    ultimo_costo = db.Column(db.NUMERIC(12,6))

class Clientes(db.Model): 
    id = db.Column(db.INTEGER, primary_key=True)
    clave = db.Column(db.SMALLINT, nullable=False, unique=True)
    nombre = db.Column(db.VARCHAR(128), nullable=False)

class Proveedores(db.Model): 
    id = db.Column(db.INTEGER, primary_key=True)
    clave = db.Column(db.SMALLINT, nullable=False, unique=True)
    nombre = db.Column(db.VARCHAR(128), nullable=False)
    credito = db.Column(db.BOOLEAN, nullable=False)
    dias_credito = db.Column(db.SMALLINT)
    dpp_dias = db.Column(db.SMALLINT)
    dpp_factor = db.Column(db.REAL)