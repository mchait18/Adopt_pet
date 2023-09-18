from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, AnyOf, Optional, URL

class AddPetForm(FlaskForm):
    name=StringField("Pet Name", validators=[InputRequired()])
    species=StringField("Species", validators=[AnyOf(("cat", "dog", "porcupine"), 
                                                     message="Species must be cat, dog or porcupine")])
    photo_url=StringField("Photo URL", validators=[Optional(), URL(message="Please submit a valid URL")])
    age=IntegerField("Age",validators=[NumberRange(min=0, max=30, message="Age must be between 0-30")])
    notes=StringField("Notes")
    
class EditPetForm(FlaskForm):
    photo_url=StringField("Photo URL", validators=[Optional(), URL(message="Please submit a valid URL")])
    notes=StringField("Notes")
    available=BooleanField("Available?")
    

    