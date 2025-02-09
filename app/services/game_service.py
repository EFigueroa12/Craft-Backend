from extensions import db
from ..models.game import Game, GamePlayers
from ..models.id_deck import IDDeck, IDDeckCard
from ..models.resource_deck import ResourceDeck, ResourceDeckCard
from ..models.hands import Hand
from ..models.inventories import Inventory
import random

def init_game(player_id):

    #create game instance
    print("making new game service")
    new_game = Game(game_status="waiting")
    db.session.add(new_game)
    db.session.flush()

    game_players = GamePlayers(game_id=new_game.id, player_id=player_id, turn_order=0)
    db.session.add(game_players)
    db.session.flush()

    #deck has game id-> deckCard has deck_id, position, and card_typepip i
    #ID deck
    id_cards = ["scissors", "rock", "paper", "cockroach"] * 4 #12 cards
    random.shuffle(id_cards)
    id_deck = IDDeck(game_id=new_game.id)
    db.session.add(id_deck)
    db.session.flush()

    hand = Hand(player_id=player_id)
    db.session.add(hand)
    db.session.flush()
    # handid = hand.query.filter_by(player_id=player_id).first()

    for order, card in enumerate(id_cards):
        id_card = IDDeckCard(deck_id=id_deck.id, card_type=card, position= order, hand_id=None)
        db.session.add(id_card)
        db.session.flush()

    #RSC deck
    rsc_cards = ["wood", "stone", "metal"] * 12 #36 resource cards
    random.shuffle(rsc_cards)
    rsc_deck = ResourceDeck(game_id=new_game.id)
    db.session.add(rsc_deck)
    db.session.flush()

    inventory = Inventory(player_id=player_id)
    db.session.add(inventory)
    db.session.flush()
    # inventoryid = inventory.query.filter_by(player_id=player_id).first()

    for order, card in enumerate(rsc_cards):
        rsc_card = ResourceDeckCard(deck_id=rsc_deck.id, card_type=card, position=order, inventory_id=None)
        db.session.add(rsc_card)
        db.session.flush()

    db.session.commit()

    return new_game.id, id_deck.id, rsc_deck.id

