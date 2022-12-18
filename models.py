from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://vistaflags.com/21655-medium_default/adopt-a-pet-ado1.jpg"
# MODELS GO BELOW!

class Pet(db.Model):
    """Pet model."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def image_url(self):
        """Return uploaded image of pet or default."""

        return self.photo_url or DEFAULT_IMAGE


def connect_db(app):
    """Connects database to Flask app."""
    db.app = app
    db.init_app(app)
    
