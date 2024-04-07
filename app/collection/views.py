
from flask import render_template, redirect, request, url_for, flash

from . import collection

from .. import db
from ..models import Collection
from ..db_operations import create, update, delete

@collection.route('/', methods=['POST', 'GET'])
def index():
    collections = Collection.query.all()
    if request.method == "POST":
        name = request.form.get('name')
        if name.isalnum() and name[0].isalpha():
            create(Collection, db, {'name': name})
        elif name.strip()=="":
            flash("Collection name should not be empty")
        else:
            flash("Collection name should only contain letters or numbers and begin with a letter")
        return redirect(url_for('.index'))
    return render_template('collection/index.html', collections=collections)


@collection.route('/delete-collection', methods=['post', 'get'])
def delete_collection():
    collection_id = int(request.args.get('collection_id'))
    delete(Collection, db, collection_id)
    return redirect(url_for('.index'))
