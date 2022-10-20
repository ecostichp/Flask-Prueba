from iacele import create_app


# Se configura el objeto 'app' (app principal de este proyecto) con las variables
# de entorno segun el ambiente que quieres trabajar:
#   -Ambiente de testeo: 'Test'
#   -Ambiente de desarrollo: 'Dev'
#   -Ambiente de producción: 'Prod'
application_environment = 'Test'



app = create_app(application_environment)




if __name__ == "__main__":
    
    print(f'\n\n\n*** Estás corriendo la aplicación en modo {application_environment}')

    app.run(debug = True)