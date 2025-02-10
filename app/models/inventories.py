from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from extensions import db

class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, ForeignKey("player.id"), nullable=False)

    resourcedeck_card = relationship("ResourceDeckCard", back_populates="inventory")
    player = relationship("Player", back_populates="inventory")

    def __repr__(self):
        return f'<Invetory(player_id={self.player_id}, resource_card_id={self.resourcedeck_card_id})>'