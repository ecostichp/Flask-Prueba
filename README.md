### IACele

La Inteligencia Artificial Cele, está diseñada para explotar el potencial de tu negocio mediante el Business Intelligence y el Análisis de Datos.



### 1. Crea un entorno en python
```
python -m venv 'nombre_env'
'nombre_env'\Scripts\activate
```


### 2. Instalar las siguientes dependencias del proyecto.
```
python -m pip install -U Pip  
python -m pip install -U Flask Psycopg2 Flask-SQLAlchemy Flask-Login Flask-WTF Pandas OpenPyXL
```

### 3. Inicia el servidor
```
python entrypoint.py
```





### Ejemplo de cómo documentar las clases y funciones del proyecto.
def suma(a: int|float, b: int|float =5) -> int|float:
    """
    Esta función sirve para sumar el número a y el número b

    Args:
        :param1 a (int | float): Es el primer número a sumar, puede ser un entero o un decimal.
        :param2 b (int | float): Es el segundo número a sumar, puede ser un entero o un decimal. Su valor default es 5.

    Returns:
        :retur c (int | float): Retorna un número, puede ser un entero o un decimal.

    Raises:
        KeyError: Raises an exception.
    """

    c = a + b
    return c

help(suma)
suma.__doc__
