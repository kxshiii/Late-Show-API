from flask import Blueprint, request, jsonify
from server.models.user import User
from server import db, bcrypt

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message' : 'User created'}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({'message' : 'Logged in successfully'}), 200
    return jsonify({'message' : 'Invalid credentials'}), 401

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message' : 'Logged out successfully'}), 200
