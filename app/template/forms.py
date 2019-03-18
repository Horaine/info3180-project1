from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    name = StringField('Last Name', validators=[DataRequired()])
    
class AddUser(FlaskForm):
    gender = Select('Gender :Males, Female')
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    Biography = StringField('Biography', validators=[DataRequired()])
    
    
class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    description = StringField('Description', validators=[DataRequired()])