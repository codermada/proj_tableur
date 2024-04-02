from flask import render_template, request, redirect, url_for

from . import home

from .. import db
from ..models import Formula

@home.route('/', methods=['POST', 'GET'])
def index():
    Formula.update()
    return redirect(url_for('collection.index'))

