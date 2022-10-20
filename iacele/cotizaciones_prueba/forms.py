from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, DateField, DecimalField, IntegerField, BooleanField



class Formulario_Cotizacion (FlaskForm):
    fecha = DateField ('Fecha')
    cliente_numero = IntegerField ('Folio Cliente')
    vendedor_numero = IntegerField ('Folio Vendedor')
    cliente_nombre = StringField ('Cliente')
    vendedor_nombre = StringField ('Vendedor')
    producto_cantidad = DecimalField ('Cantidad')
    producto_codigo = StringField ('Código')
    producto_descripcion = StringField ('Descripción')
    correcto = BooleanField ('Correcto')
    guardar = SubmitField ('Guardar')