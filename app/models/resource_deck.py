from extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SAEnum, ForeignKey
from enum import Enum

class ResourceDeck(db.Model):
    __tablename__ = 'resource_deck'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, ForeignKey("game.id"), nullable=False)

    cards = relationship("ResourceDeckCard", back_populates="deck", cascade="all, delete-orphan")
    game = relationship("Game", back_populates="rsc_decks")

    def _repr__(self):
        return f'<ResourceDeck (game_id= {self.game_id})>'

class ResourceCardType(Enum):
    WOOD= "wood"
    STONE= "stone"
    METAL= "metal"

class ResourceDeckCard(db.Model):
    __tablename__ = 'resource_deck_card'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deck_id = db.Column(db.Integer, ForeignKey("resource_deck.id"), nullable=False)
    card_type = db.Column(SAEnum(ResourceCardType), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    deck = relationship("ResourceDeck", back_populates="cards")

    inventory_id = db.Column(db.Integer, ForeignKey("inventory.id"), nullable=True)
    inventory = relationship("Inventory", back_populates="resourcedeck_card")

    def __repr__(self):
        return f'<ResourceDeckCard (deck_id = {self.deck_id}, card_type={self.card_type.value}, position={self.position})>'