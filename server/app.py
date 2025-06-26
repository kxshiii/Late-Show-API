from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from server.controllers.auth_controller import auth_blueprint
app.register_blueprint(auth_blueprint)

