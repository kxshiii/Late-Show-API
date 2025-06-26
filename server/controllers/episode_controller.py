from flask import Blueprint, request, jsonify
from server.models.episode import Episode
from server import db

episode_blueprint = Blueprint('episode', __name__)


@episode_blueprint.route('/episode', methods=['POST'])
def add_episode():
    data = request.get_json()
    new_episode = Episode(title=data['title'], description=data['description'], air_date=data['air_date'])
    db.session.add(new_episode)
    db.session.commit()
    return jsonify({'message' : 'New episode added'}), 201


@episode_blueprint.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    output = []
    for episode in episodes:
        episode_data = {}
        episode_data['id'] = episode.id
        episode_data['title'] = episode.title
        episode_data['description'] = episode.description
        episode_data['air_date'] = episode.air_date
        output.append(episode_data)
    return jsonify({'episodes' : output})
