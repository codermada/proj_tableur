
from flask import Blueprint

table = Blueprint('table', __name__)

from . import views

