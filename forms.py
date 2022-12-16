from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet's Name")
    species = StringField("Pet's Species")
    photo_url = StringField("Pet's Photo URL")
    age = IntegerField("Pet's Age")
    notes = StringField("Notes")
