from flask_wtf import FlaskForm
from wtforms.fields import SubmitField



class Formulario_Inser_Bulk_Data (FlaskForm):
    guardar = SubmitField ('Guardar')