from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet's Name", validators = [InputRequired(message="Name field cannot be blank.")])
    species = SelectField("Pet's Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("hamster", "Hamster"), ("bird", "Bird"),
             ("fish", "Fish"), ("turtle", "Turtle"), ("snake", "Snake"),("rabbit", "Rabbit")])
    photo_url = StringField("Pet's Photo URL", validators = [Optional(), URL(message="Input must be a valid URL.")])
    age = IntegerField("Pet's Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30.")])
    notes = TextAreaField("Notes", validators = [Optional()])
    available = BooleanField("Available?")


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    
    name = StringField("Pet's Name", validators = [InputRequired(message="Name field cannot be blank.")])
    species = SelectField("Pet's Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("hamster", "Hamster"), ("bird", "Bird"),
             ("fish", "Fish"), ("turtle", "Turtle"), ("snake", "Snake"),("rabbit", "Rabbit")])
    photo_url = StringField("Pet's Photo URL", validators = [Optional(), URL(message="Input must be a valid URL.")])
    age = IntegerField("Pet's Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30.")])
    notes = TextAreaField("Notes", validators = [Optional()])
    available = BooleanField("Available?")