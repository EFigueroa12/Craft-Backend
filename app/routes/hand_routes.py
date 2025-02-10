from flask import Blueprint, request, jsonify
from extensions import db
from ..models.player import Player
from ..models.hands import Hand
from ..models.id_deck import IDDeckCard

hand_bp = Blueprint('hand', __name__)

@hand_bp.route('/new_hand/<int:player_id>', methods=["GET"])
def new_hand(player_id):
    player = db.session.get(Player, player_id)
    if not player:
        return jsonify({'error':'Player not found'}), 400
    hand = Hand.query.filter_by(player_id= player.id).order_by(Hand.id.asc()).first()
    if not hand:
        return jsonify({'error':"Player's Hand not found"}), 400

    cards = IDDeckCard.query.filter_by(hand_id= hand.id).all()
    return jsonify([card.to_dict() for card in cards])