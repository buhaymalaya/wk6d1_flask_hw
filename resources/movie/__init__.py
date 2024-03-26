from flask_smorest import Blueprint

bp = Blueprint("movie", __name__, description="Routes for Movies")

from . import routes