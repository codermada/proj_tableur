cd app
mkdir $1
cd $1
touch views.py
echo """
from flask import Blueprint

$1 = Blueprint('$1', __name__)

from . import views
""" > __init__.py
echo """
from flask import render_template

from . import $1

@$1.route('/')
def index():
    return render_template('$1/index.html')
""" > views.py
cd ..
cd templates
mkdir $1
cd $1
echo """
{% extends "base.html" %}

{% block content %}

{% endblock content %}
""" > index.html
