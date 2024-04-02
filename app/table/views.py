from flask import render_template, redirect, request, url_for

from . import table

from .. import db
from ..models import Collection, Table, Formula, Cell
from ..db_operations import create, update, delete
from ..function_analyzer import nb_params, param_names
from ..formulas import *

@table.route('/', methods=['post', 'get'])
def index():
    collection_id = int(request.args.get('collection_id'))
    collection = Collection.query.get(collection_id)
    formulas = Formula.query.all()
    tables = Table.query.filter_by(collection_id = collection_id).order_by(Table.id.desc()).all()
    return render_template('table/index.html', collection=collection, formulas=formulas, tables=tables)

@table.route('/create-table', methods=['post', 'get'])
def create_table():
    collection_id = int(request.args.get('collection_id'))
    if request.method == 'POST':
        create(Table, db, {'name': request.form.get('name'),'collection_id': collection_id})
        return redirect(url_for('.index', collection_id=collection_id))
    return redirect(url_for('.index', collection_id=collection_id))

@table.route('/delete-table', methods=['post', 'get'])
def delete_table():
    collection_id = int(request.args.get('collection_id'))
    table_id = int(request.args.get('table_id'))
    delete(Table, db, table_id)
    return redirect(url_for('.index', collection_id=collection_id))


@table.route('/choose-formula', methods=['post', 'get'])
def choose_formula():
    formula_id = int(request.form.get('formula_name'))
    formula = Formula.query.get(formula_id)
    collection_id = int(request.args.get('collection_id'))
    table_id = int(request.args.get('table_id'))
    update_str = "update(Table, db, {'formula_name': "+f"'{formula.name}'"+",'script': "+f"\"\"\"{formula.script}\"\"\""+",'param_names': param_names("+formula.name+"), 'n_col': nb_params("+formula.name+")},table_id)"
    script = formula.script+"\n{}"
    exec(script.format((update_str)))
    return redirect(url_for('.index', collection_id=collection_id))

@table.route('/add-record', methods=['post', 'get'])
def add_record():
    collection_id = int(request.args.get('collection_id'))
    table_id = int(request.args.get('table_id'))
    table = Table.query.get(table_id)
    add_record_str = """
for key, value in {**dict(request.form),**{f"'{table.formula_name}'": """+table.formula_name+"""(**dict(request.form))}}.items():
    create(Cell, db, {'key': key, 'value': value, 'table_id': table_id})"""
    script = table.script + "\n{}"
    exec(script.format((add_record_str)))
    return redirect(url_for('.index', collection_id=collection_id))