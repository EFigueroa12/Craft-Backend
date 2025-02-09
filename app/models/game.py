from extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SAEnum, ForeignKey
from enum import Enum

class GameStatus(Enum):
    WAITING= "waiting"
    ACTIVE="active"
    FINISHED="finished"

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_status = db.Column(SAEnum(GameStatus), nullable=False)
    # current_turn_player_id = db.Column(db.Integer, ForeignKey("game_player.id"), nullable=False)

    current_turn_player = relationship("GamePlayers", back_populates="game", cascade="all, delete")

    rsc_decks = relationship("ResourceDeck", back_populates="game", cascade="all, delete")
    id_decks = relationship("IDDeck", back_populates="game", cascade="all, delete")

    # game_players = relationship("GamePlayers", back_populates="game")
    game_turns = relationship("Turns", back_populates="game", cascade="all, delete")


    def __repr__(self):
        return f'<Game(game_id={self.id}, game_status={self.game_status})>'

class GamePlayers(db.Model):
    __tablename__ = 'game_players'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, ForeignKey("game.id"), nullable=False)
    player_id =db.Column(db.Integer, ForeignKey("player.id"), nullable=False)
    turn_order = db.Column(db.Integer, nullable=False)


    game = relationship("Game", back_populates="current_turn_player")
    player = relationship("Player", back_populates="game_players")

    def __repr__(self):
        return f'<GamePlayers(game_id={self.game_id}, player_id={self.player_id})>'


class Turns(db.Model):
    __tablename__ = 'turns'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, ForeignKey("game.id"), nullable=False)
    player_id =db.Column(db.Integer, ForeignKey("player.id"), nullable=False)
    turn_number = db.Column(db.Integer, nullable=False)
    action = db.Column(db.Text)

    game = relationship("Game", back_populates="game_turns")
    player = relationship("Player", back_populates="player_turn")

    def __repr__(self):
        return f'<Turns(game_id={self.game_id}, player_id={self.player_id}, turn_num={self.turn_number}, action={self.action})>'