# Se importan las librerías necesarias para este Proyecto (app principal).
from flask import Flask

# Se importan las librerías necesarias para configurar el redireccionamiento de
# la única URL global a la URL 'Home' del proyecto.


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



def create_app(application_environment):
    
    # Se instancía la clase Flask para generar el objeto 'app', que es la
    # aplicación principal del proyecto 'iacele'. Todavía no tiene cargada
    # ninguna configuración.
    app = Flask(__name__, instance_relative_config = True)


    if application_environment == 'Test':
        app.config.from_pyfile('testConfig.py')
    elif application_environment == 'Dev':
        app.config.from_pyfile('devConfig.py')
    else:
        app.config.from_pyfile('prodConfig.py')


    db.init_app(app)


    with app.app_context():
        
        # Se importa y registra cada blueprint (sub-apps que conforman la app principal), necesario
        # para la vistas de este proyecto.
        from iacele.frontend import frontend
        app.register_blueprint(frontend)

        from iacele.dashboard import dashboard
        app.register_blueprint(dashboard)

        from iacele.authentication import authentication
        app.register_blueprint(authentication)

        from iacele.cotizaciones_prueba import cotizaciones_prueba
        app.register_blueprint(cotizaciones_prueba)

        from iacele.database import database
        app.register_blueprint(database)

        # Se crea las tablas. Se tiene que haber importado los blueprint para que la instrucción
        # siguiente contemple las tablas de sus modelos correspondientes.
        db.create_all()

        return app