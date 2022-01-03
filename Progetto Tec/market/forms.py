from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, validators, Form
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
from flask_wtf.file import FileAllowed, FileField, FileRequired

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Indirizzo Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Conferma Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Crea Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Accedi')



class Addproducts(Form):
    nome = StringField('Nome prodotto', [validators.DataRequired()])
    price = IntegerField('Prezzo', [validators.DataRequired()])
    caution = IntegerField('Cauzione', [validators.DataRequired()])
    province = StringField('Provincia', validators=[Length(max=2), DataRequired()])
    description = TextAreaField('Descrizione', validators=[Length(max=180), DataRequired()])
    submit = SubmitField(label='Inserisci Annuncio')
    image_1 = FileField('Prima immagine', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_2 = FileField('Seconda immagine', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])