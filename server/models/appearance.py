from server.app import db

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hex_code = db.Column(db.String(100), nullable=False)
    guests = db.relationship('Guest', backref='appearance', cascade='all, delete-orphan', lazy=True)
    episodes = db.relationship('Episode', backref='appearance', cascade='all, delete-orphan', lazy=True)        
