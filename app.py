from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "shhhh...secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

########################################################
# Routes:
########################################################

@app.route("/", methods = ["GET"])
def show_homepage():
    """Show homepage with list of pets."""

    pets = Pet.query.order_by(Pet.name).all()

    return render_template("homepage.html", pets=pets)


@app.route("/add", methods = ["GET"])
def show_add_pet_form():
    """Show add pet form."""
 
    form = AddPetForm()

    return render_template("add_pet.html", form=form)


@app.route("/add",  methods = ["POST"])
def handle_adding_pet():
    """Handle add pet form submission."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_ure = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        db.session.commit()
        flash(f"{name} the {species} added!")
        return redirect("/add")

