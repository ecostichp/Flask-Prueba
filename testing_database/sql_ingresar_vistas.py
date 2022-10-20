import sqlite3
from sql_conexion import create_connection



# El siguiente código crea una vista en SQLite para visualizar las cotizaciones de manera sencilla.

def create_views():
    ''' Función que crea las vistas a las
        tablas del proyecto.
    '''

    conn = create_connection()
    c = conn.cursor()

    query_vista_cotizaciones = '''
    CREATE VIEW vista_cotizaciones 

    AS 

    SELECT 

    cot.numero,
    cot.fecha,
    cot.cliente,
    cli.nombre,
    cot.vendedor,
    ven.nombre,

    cot.renglon_art01,
    cot.cantidad_art01,
    cot.codigo_art01,
    pro01.descripcion,
    pro01.ultimo_costo,
    cot.descuento_art01,

    cot.renglon_art02,
    cot.cantidad_art02,
    cot.codigo_art02,
    pro02.descripcion,
    pro02.ultimo_costo,
    cot.descuento_art02,

    cot.renglon_art03,
    cot.cantidad_art03,
    cot.codigo_art03,
    pro03.descripcion,
    pro03.ultimo_costo,
    cot.descuento_art03,

    cot.renglon_art04,
    cot.cantidad_art04,
    cot.codigo_art04,
    pro04.descripcion,
    pro04.ultimo_costo,
    cot.descuento_art04,

    cot.renglon_art05,
    cot.cantidad_art05,
    cot.codigo_art05,
    pro05.descripcion,
    pro05.ultimo_costo,
    cot.descuento_art05,

    cot.renglon_art06,
    cot.cantidad_art06,
    cot.codigo_art06,
    pro06.descripcion,
    pro06.ultimo_costo,
    cot.descuento_art06,

    cot.renglon_art07,
    cot.cantidad_art07,
    cot.codigo_art07,
    pro07.descripcion,
    pro07.ultimo_costo,
    cot.descuento_art07,

    cot.renglon_art08,
    cot.cantidad_art08,
    cot.codigo_art08,
    pro08.descripcion,
    pro08.ultimo_costo,
    cot.descuento_art08,

    cot.renglon_art09,
    cot.cantidad_art09,
    cot.codigo_art09,
    pro09.descripcion,
    pro09.ultimo_costo,
    cot.descuento_art09,

    cot.renglon_art10,
    cot.cantidad_art10,
    cot.codigo_art10,
    pro10.descripcion,
    pro10.ultimo_costo,
    cot.descuento_art10,

    cot.renglon_art11,
    cot.cantidad_art11,
    cot.codigo_art11,
    pro11.descripcion,
    pro11.ultimo_costo,
    cot.descuento_art11,

    cot.renglon_art12,
    cot.cantidad_art12,
    cot.codigo_art12,
    pro12.descripcion,
    pro12.ultimo_costo,
    cot.descuento_art12,

    cot.renglon_art13,
    cot.cantidad_art13,
    cot.codigo_art13,
    pro13.descripcion,
    pro13.ultimo_costo,
    cot.descuento_art13,

    cot.renglon_art14,
    cot.cantidad_art14,
    cot.codigo_art14,
    pro14.descripcion,
    pro14.ultimo_costo,
    cot.descuento_art14,

    cot.renglon_art15,
    cot.cantidad_art15,
    cot.codigo_art15,
    pro15.descripcion,
    pro15.ultimo_costo,
    cot.descuento_art15,

    cot.renglon_art16,
    cot.cantidad_art16,
    cot.codigo_art16,
    pro16.descripcion,
    pro16.ultimo_costo,
    cot.descuento_art16,

    cot.renglon_art17,
    cot.cantidad_art17,
    cot.codigo_art17,
    pro17.descripcion,
    pro17.ultimo_costo,
    cot.descuento_art17,

    cot.renglon_art18,
    cot.cantidad_art18,
    cot.codigo_art18,
    pro18.descripcion,
    pro18.ultimo_costo,
    cot.descuento_art18,

    cot.renglon_art19,
    cot.cantidad_art19,
    cot.codigo_art19,
    pro19.descripcion,
    pro19.ultimo_costo,
    cot.descuento_art19,

    cot.renglon_art20,
    cot.cantidad_art20,
    cot.codigo_art20,
    pro20.descripcion,
    pro20.ultimo_costo,
    cot.descuento_art20

    FROM Cotizaciones cot

    LEFT JOIN Clientes cli ON cot.cliente = cli.codigo
    LEFT JOIN Vendedores ven ON cot.vendedor = ven.clave
    LEFT JOIN Productos pro01 ON pro01.codigo = cot.codigo_art01
    LEFT JOIN Productos pro02 ON pro02.codigo = cot.codigo_art02
    LEFT JOIN Productos pro03 ON pro03.codigo = cot.codigo_art03
    LEFT JOIN Productos pro04 ON pro04.codigo = cot.codigo_art04
    LEFT JOIN Productos pro05 ON pro05.codigo = cot.codigo_art05
    LEFT JOIN Productos pro06 ON pro06.codigo = cot.codigo_art06
    LEFT JOIN Productos pro07 ON pro07.codigo = cot.codigo_art07
    LEFT JOIN Productos pro08 ON pro08.codigo = cot.codigo_art08
    LEFT JOIN Productos pro09 ON pro09.codigo = cot.codigo_art09
    LEFT JOIN Productos pro10 ON pro10.codigo = cot.codigo_art10
    LEFT JOIN Productos pro11 ON pro11.codigo = cot.codigo_art11
    LEFT JOIN Productos pro12 ON pro12.codigo = cot.codigo_art12
    LEFT JOIN Productos pro13 ON pro13.codigo = cot.codigo_art13
    LEFT JOIN Productos pro14 ON pro14.codigo = cot.codigo_art14
    LEFT JOIN Productos pro15 ON pro15.codigo = cot.codigo_art15
    LEFT JOIN Productos pro16 ON pro16.codigo = cot.codigo_art16
    LEFT JOIN Productos pro17 ON pro17.codigo = cot.codigo_art17
    LEFT JOIN Productos pro18 ON pro18.codigo = cot.codigo_art18
    LEFT JOIN Productos pro19 ON pro19.codigo = cot.codigo_art19
    LEFT JOIN Productos pro20 ON pro20.codigo = cot.codigo_art20
        
    '''

    if conn != None:
        try:
            c.execute(query_vista_cotizaciones)
            conn.commit()
            conn.close()
            print('Las vistas se crearon con éxito.')
        except sqlite3.Error as e:
            print('Falló la creación de las vistas. El error es:', e)
    
    else:
        print('La conexión a la base de datos es Nula')



if __name__ == '__main__':
    create_views()