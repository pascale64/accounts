from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from bdf.models import Auxilliere


class AddAuxilliereForm(FlaskForm):
    id = StringField('auxilliere', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Sign In')

