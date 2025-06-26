from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server import db

appearance_blueprint = Blueprint('appearance', __name__)

@appearance_blueprint.route('/appearance', methods=['GET'])
def get_appearance():
    appearance = Appearance.query.all()
    output = []
    for a in appearance:
        appearance_data = {}
        appearance_data['id'] = a.id
        appearance_data['name'] = a.name
        appearance_data['hex_code'] = a.hex_code
        output.append(appearance_data)
    return jsonify({'appearance' : output})

@appearance_blueprint.route('/appearance', methods=['POST'])
def add_appearance():
    data = request.get_json()
    new_appearance = Appearance(name=data['name'], hex_code=data['hex_code'])
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify({'message' : 'New appearance added'})
