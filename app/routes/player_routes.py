from flask import Blueprint, request, jsonify
from ..models.player import Player
from extensions import db

player_bp = Blueprint('player', __name__)

@player_bp.route('/create_player', methods=["POST"])

def create_player():
    data = request.json
    username = data.get("username")

    if not username:
        return jsonify({'error':'missing username'}), 404
    
    if Player.query.filter_by(username=username).first():
        return jsonify({'error':'Username already used.'}), 404

    new_player = Player(username=username)
    try:
        db.session.add(new_player)
        db.session.commit()
        return jsonify({'message': 'Created new player!', 'player_id': new_player.id, 'username': new_player.username})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@player_bp.route('/player/<int:user_id>', methods=['GET'])
def get_player(user_id):
    player = Player.query.get(user_id)
    if player:
        return jsonify({"player_id":player.id, "username":player.username}), 200
    return jsonify({'error':'user not found'}), 404