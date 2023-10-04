from flask_sqlalchemy import SQLALchemy

GENERIC_IMAGE = "https://cdn2.vectorstock.com/i/1000x1000/42/16/lost-dog-sign-sketch-icon-vector-13294216.jpg"

db = SQLALchemy()

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

def image_url(self):
    """Return an image for a pet."""

    return self.photo_url or GENERIC_IMAGE

def connect_db(app):
    "Connects database to Flask application."

    db.app = app
    db.init_app(app)

