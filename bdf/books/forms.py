from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField,\
                    FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from bdf.models import Book 


class AddBookForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    date = DateField('date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    debit = IntegerField('Debit')
    credit = IntegerField('Credit')
    montant = FloatField('Montant', validators=[DataRequired()])
    AUX = StringField('Auxilliare')
    TP = StringField('Type')
    REF = StringField('REF')
    JN = StringField('JN')
    PID = IntegerField('PID')
    CT = IntegerField('CT')
    submit = SubmitField('Submit')
    modify = SubmitField('Modify')
    delete = SubmitField('Delete')
