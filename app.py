from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "shhhh...secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

debug = DebugToolbarExtension(app)

########################################################
# Routes:
########################################################

@app.route("/", methods = ["GET"])
def show_homepage():
    """Show homepage with list of pets."""

    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)


@app.route("/add", methods = ["GET", "POST"])
def show_add_pet_form():
    """Show/handle add pet form."""
 
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data,
            available = form.available.data
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} the {new_pet.species} added!")
        return redirect("/")
    else:
        return render_template(f"add_pet.html", form=form)


@app.route("/pet_details/<int:id>", methods = ["GET"])
def show_pet_details(id):
    """Shows details page for a specific pet."""

    pet = Pet.query.get_or_404(id)
    return render_template("pet_details.html", pet=pet)


@app.route("/edit_pet/<int:id>", methods = ["GET", "POST"]) 
def edit_pet_details(id):
    """Edit details about a specific pet."""
    

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    print("#####")
    print(pet)

    if form.validate_on_submit():
        pet.name = form.name.data,
        pet.species = form.species.data,
        pet.photo_url = form.photo_url.data,
        pet.age = form.age.data,
        pet.notes = form.notes.data,
        pet.available = form.available.data
        db.session.commit()

        flash(f"{pet.name} the {pet.species} updated!")

        return redirect("/")
    else:
        return render_template("edit_pet.html", form=form, pet=pet)