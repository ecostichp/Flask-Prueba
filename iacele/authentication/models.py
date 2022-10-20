# Se importan las librerías necesarias para el modelo de este blueprint (sub-app).
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# Se importa el objeto 'db' desde el proyecto. El 'modelo' utilizará este objeto
# para comunicarse, a través de SQLAlchemy, con el motor de base de datos que se
# configuró en las variables de ambiente de entorno.
from iacele import db



# Se genera la clase User. Con este modelo, se genera la tabla User en la base de
# datos del proyecto. En esta tabla se registran los datos generales de los usuarios
# del proyecto. Se usará para el módulo de RH, permisos dentro de esta app, etc.
class Usuarios(db.Model, UserMixin): 
    id = db.Column(db.INTEGER, primary_key=True)
    usuario = db.Column(db.VARCHAR(16), nullable=False, unique=True)
    nombre_1ro = db.Column(db.VARCHAR(16), nullable=False)
    nombre_2do = db.Column(db.VARCHAR(16))
    apellido_paterno = db.Column(db.VARCHAR(16), nullable=False)
    apellido_materno = db.Column(db.VARCHAR(16), nullable=False)
    almacen = db.Column(db.SMALLINT, nullable=False)
    foto = db.Column(db.VARCHAR(16))
    contraseña = db.Column(db.VARCHAR(128), nullable=False)


    # Esta función utiliza la librería wekzeug.security para hacer un hash de la
    # contraseña proporcionada y la asigna al atributo del objeto.
    def set_password(self, contraseña):
            self.contraseña = generate_password_hash(contraseña)


    # Esta función utiliza la librería wekzeug.security para checar que la contraseña
    # ingresada coincide con la contraseña. Devuelve un un booleano.
    def verify_password(self, contraseña):
            return check_password_hash (self.contraseña, contraseña)


    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return '<Usuario %r>' % self.usuario
    

    # Los siguientes métodos de la clase, devuelven al objeto del usuario buscado.
    # Si no lo encuentra, devuelve un None.
    @staticmethod
    def get_by_id(id):
        return Usuarios.query.get(id)
    

    @staticmethod
    def get_by_user(usuario):
        return Usuarios.query.filter_by(usuario=usuario).first()


    #El siguiente método de la clase, devuelve una lista con todos los objetos
    # registrados en la tabla Users). Si no hay ninguno, devuelve una lista vacía.
    @staticmethod
    def get_all():
        return Usuarios.query.all()