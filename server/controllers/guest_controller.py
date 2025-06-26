from flask import Blueprint, request, jsonify
from server.models.guest import Guest
from server import db

guest_blueprint = Blueprint('guest', __name__)


@guest_blueprint.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    output = []
    for guest in guests:
        guest_data = {}
        guest_data['id'] = guest.id
        guest_data['name'] = guest.name
        guest_data['age'] = guest.age
        guest_data['gender'] = guest.gender
        output.append(guest_data)
    return jsonify({'guests' : output})


@guest_blueprint.route('/guest', methods=['POST'])
def add_guest():
    data = request.get_json()
    new_guest = Guest(name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(new_guest)
    db.session.commit()
    return jsonify({'message' : 'New guest added'}), 201
