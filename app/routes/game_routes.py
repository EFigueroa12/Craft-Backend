from flask import Blueprint, request, jsonify
from extensions import db
from ..models.player import Player
from ..models.game import Game, GamePlayers
from ..services.game_service import init_game
from ..models.hands import Hand

game_bp = Blueprint('game', __name__)

@game_bp.route('/new_game', methods=["POST"])

def create_game():
    print("received request to make game")
    data = request.json
    player_id = data.get("playerId")

    if not player_id:
        return jsonify({'error':'missing player ID'}), 404
    
    player = db.session.get(Player, player_id)
    if not player:
        return jsonify({'error': 'player not found'}), 404
    
    existing_game = GamePlayers.query.filter_by(player_id= player_id).first()
    print(existing_game)
    if existing_game:
        return jsonify({'message':'Game exists', 'game_id':existing_game.game_id})
    
    game_id, id_deck, rsc_deck = init_game(player_id)
    return jsonify({'message':'game created!', 'game_id':game_id, 'id_deck': id_deck, 'rsc_deck':rsc_deck})

@game_bp.route('/end_game/<int:game_id>', methods=["DELETE"])
def end_game(game_id):
    game = db.session.get(Game, game_id) 
    if not game:
        return jsonify({'error':'game not found'}), 404
    gamePlayer = GamePlayers.query.filter_by(game_id= game.id).first()
    if not gamePlayer:
        return jsonify({'error':'Player in game not found'})
    hand = Hand.query.filter_by(player_id= gamePlayer.player_id).order_by(Hand.id.asc()).first()
    if not hand:
        return jsonify({'error': 'Hand not found for player.'})
    db.session.delete(hand)
    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'game successfully deleted.'})
    
