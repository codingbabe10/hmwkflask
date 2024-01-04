from flask_smorest import Blueprint

bp = Blueprint('recipes', __name__, description='Ops on recipes', url_prefix='/recipes')

from . import routes