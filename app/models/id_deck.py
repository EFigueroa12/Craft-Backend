from extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SAEnum, ForeignKey
from enum import Enum

class IDDeck(db.Model):
    __tablename__ = 'id_deck'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, ForeignKey("game.id"), nullable=False)

    cards = relationship("IDDeckCard", back_populates="deck", cascade="all, delete-orphan")
    game = relationship("Game", back_populates="id_decks")

    def _repr__(self):
        return f'<IDDeck (game_id= {self.game_id})>'

class CardType(Enum):
    SCISSORS= "scissors"
    ROCK= "rock"
    PAPER= "paper"
    COCKROACH= "cockroach"

class IDDeckCard(db.Model):
    __tablename__ = 'id_deck_card'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deck_id = db.Column(db.Integer, ForeignKey("id_deck.id"), nullable=False)
    card_type = db.Column(SAEnum(CardType), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    deck = relationship("IDDeck", back_populates="cards")
    
    hand_id = db.Column(db.Integer, ForeignKey("hand.id"), nullable=True)
    hand = relationship("Hand", back_populates="iddeck_card")

    def to_dict(self):
        return {
            "id": self.id,
            "deck_id": self.deck_id,
            "hand_id":self.hand_id,
            "card_type": self.card_type.value,
            "position": self.position
        }

    def __repr__(self):
        return f'<IDDeckCard (deck_id = {self.deck_id}, card_type={self.card_type.value}, position={self.position})>'