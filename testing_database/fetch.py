from db_connect import connect, error_postgresql, error_sqlite



def fecth(ambiente):
    
    # Se crea la conexión a la base de datos
    conn = connect(ambiente)
    
    if conn is not None:
    
        try:
            # Se intenta crear el cursor para ejecutar órdenes en la base de datos
            cur = conn.cursor()
            
            # execute a statement
            cur.execute("SELECT row_to_json(usuarios) FROM usuarios")

            usuarios = cur.fetchone()
            
            print(usuarios)        

            cur.close()

        except (error_postgresql) as ep:
            print(ep)
        except (error_sqlite) as es:
            print(es)
        
        finally:
            conn.close()


if __name__ == '__main__':
    fecth('Development')