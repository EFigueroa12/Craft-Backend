from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from extensions import db

class Hand(db.Model):
    __tablename__ = 'hand'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, ForeignKey("player.id"), nullable=False)
    # iddeck = db.Column(db.Integer, ForeignKey("id_deck.id"), nullable=False)

    iddeck_card = relationship("IDDeckCard", back_populates="hand")
    player = relationship("Player", back_populates="hand")

    def __repr__(self):
        return f'<Hand(player_id={self.player_id})>'