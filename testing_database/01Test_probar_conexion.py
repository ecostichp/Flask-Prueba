import sqlite3

from db_connect import DATABASE_TEST



def connect_to_test_db():
    
    conn = None
    try:

        # connect to the SQLite local
        print('\nTratando de conectarse a SQLite, de manera local...')
        conn = sqlite3.connect(DATABASE_TEST)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('>>> ¡Conexión exitosa! La versión de la base de datos de SQLite es:')
        cur.execute('SELECT sqlite_version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchall()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, sqlite3.Error) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Se cerró la conexión a la base de datos.\n')


if __name__ == '__main__':
    connect_to_test_db()