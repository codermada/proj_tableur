
from flask import Blueprint

formula = Blueprint('formula', __name__)

from . import views

