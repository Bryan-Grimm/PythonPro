from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, fields
from wtforms.validators import DataRequired

class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-type Password', validators=[DataRequired()])

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class Contact(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = fields.TextAreaField("Message", validators=[DataRequired()],
                                   render_kw=({"rows": 10, "cols": 30}))
