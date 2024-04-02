
from flask import render_template, redirect, request, url_for

from . import collection

from .. import db
from ..models import Collection
from ..db_operations import create, update, delete

@collection.route('/', methods=['POST', 'GET'])
def index():
    collections = Collection.query.all()
    if request.method == "POST":
        create(Collection, db, {'name': request.form.get('name')})
        return redirect(url_for('.index'))
    return render_template('collection/index.html', collections=collections)
