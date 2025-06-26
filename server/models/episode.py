from server import db
from server.models.appearance import Appearance

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    air_date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan', lazy=True)

    def __repr__(self):
        return f"Episode('{self.title}', '{self.air_date}')"

