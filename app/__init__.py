from flask import Flask
from flask_smorest import Api

# from flask_cors import CORS 
# after installations pip etc

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# CORS(app)

db = SQLAlchemy(app) #instantiate
migrate = Migrate(app, db) 

from models.director_model import DirectorModel
from models.movie_model import MovieModel

from resources.movie import bp as movie_bp
app.register_blueprint(movie_bp)
from resources.director import bp as director_bp
app.register_blueprint(director_bp)

