from extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    
    # game_id = db.Column(db.Integer, ForeignKey("game.id"), nullable=False)

    hand = relationship("Hand", back_populates="player", cascade="all, delete-orphan")
    inventory = relationship('Inventory', back_populates="player", cascade="all, delete-orphan")

    # game = relationship("Game", back_populates="current_player")
    game_players = relationship("GamePlayers", back_populates="player")
    player_turn = relationship("Turns", back_populates="player")

    def _repr__(self):
        return f'<User {self.username}>'

