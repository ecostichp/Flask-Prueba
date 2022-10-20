import psycopg2
import sqlite3


error_postgresql = psycopg2.DatabaseError
error_sqlite = sqlite3.Error


DATABASE_TEST = 'testing_database/testSQLite.db'


DATABASE_DEV = {
        'host' : "34.94.126.128",
        'database': "lacasadelcarpintero",
        'user':"liccostich",
        'password':"e123456"
        }


usuario_db_grant = 'iacele_app'



def connect(ambiente):
    
    conn = None

    try:
        if ambiente == 'Development':
            conn = psycopg2.connect(**DATABASE_DEV)
            return conn
        
        elif ambiente == 'Testing':
            conn = sqlite3.connect(DATABASE_TEST)
            return conn
    
    except:
        return conn