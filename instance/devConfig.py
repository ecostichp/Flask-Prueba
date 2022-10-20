AMBIENTE = 'Development'

DEBUG = True

TESTING = True

SECRET_KEY = 'lacasadelcarpintero'

DATABASE_DEV = {
        'host' : "34.94.126.128",
        'database': "lacasadelcarpintero",
        'user':"iacele_app",
        'password':"iacele123456"
        }

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DATABASE_DEV['user']}:{DATABASE_DEV['password']}@{DATABASE_DEV['host']}/{DATABASE_DEV['database']}"

SQLALCHEMY_TRACK_MODIFICATIONS = False