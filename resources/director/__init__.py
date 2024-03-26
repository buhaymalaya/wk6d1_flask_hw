from flask_smorest import Blueprint

bp = Blueprint('director', __name__, description= "Routes for Directors")

from . import routes