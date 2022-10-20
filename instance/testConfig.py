AMBIENTE = 'Testing'

DEBUG = True

TESTING = True

SECRET_KEY = 'lacasadelcarpintero'

DATABASE_TEST = '../testing_database/testSQLite.db'

SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_TEST}"

SQLALCHEMY_TRACK_MODIFICATIONS = False