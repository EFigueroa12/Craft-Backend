from flask import Flask
from config import Config
from extensions import db
from flask_cors import CORS
from flask_migrate import Migrate
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins=["http://localhost:3000"])
    db.init_app(app)
    migrate = Migrate(app, db)
    from .routes.player_routes import player_bp
    from .routes.game_routes import game_bp
    from .routes.hand_routes import hand_bp
    app.register_blueprint(player_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(hand_bp)
    from .models.game import Game, GamePlayers, Turns
    from .models.id_deck import IDDeck, IDDeckCard
    from .models.resource_deck import ResourceDeck, ResourceDeckCard
    from .models.inventories import Inventory
    from .models.hands import Hand
    return app

