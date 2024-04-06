from flask import render_template, redirect, request, url_for, flash
from datetime import datetime

from . import table

from .. import db
from ..models import Collection, Table, Formula, Cell
from ..db_operations import create, update, delete
from ..function_analyzer import nb_params, param_names
from ..formulas import *
from ..csv_operation import get_data



@table.route('/', methods=['post', 'get'])
def index():
    collection_id = int(request.args.get('collection_id'))
    collection = Collection.query.get(collection_id)
    formulas = Formula.query.all()
    tables = Table.query.filter_by(collection_id = collection_id).order_by(Table.id.desc()).all()
    return render_template('table/index.html', collection=collection, formulas=formulas, tables=tables, focus=0)

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
    try:
        update_str = "update(Table, db, {'formula_name': "+f"'{formula.name}'"+",'script': "+f"\"\"\"{formula.script}\"\"\""+",'param_names': param_names("+formula.name+"), 'n_col': nb_params("+formula.name+")},table_id)"
        script = formula.script+"\n{}"
        exec(script.format((update_str)))
    except:
        flash("The name of the formula should be the same as defined in the script")
    return redirect(url_for('.index', collection_id=collection_id))

@table.route('/add-record', methods=['post', 'get'])
def add_record():
    collection_id = int(request.args.get('collection_id'))
    table_id = int(request.args.get('table_id'))
    focused = int(request.args.get('focused'))
    table = Table.query.get(table_id)
    try:
        form_data = {}
        for key, value in dict(request.form).items():
            form_data.update({key: float(value)})
        add_record_str = """
for key, value in {**form_data,**{f"{table.formula_name}": """+table.formula_name+"""(**form_data)}}.items():
    create(Cell, db, {'key': key, 'value': value, 'table_id': table_id, 'created': datetime.utcnow()})"""
        script = table.script + "\n{}"
        exec(script.format((add_record_str)))
    except:
        flash("Values should be numbers")
    if focused == 0:
        return redirect(url_for('.index', collection_id=collection_id))
    elif focused == 1:
        return redirect(url_for('.view_table', table_id=table_id, collection_id=collection_id))


@table.route('/add-records', methods=['post', 'get'])
def add_records():
    collection_id = int(request.args.get('collection_id'))
    table_id = int(request.args.get('table_id'))
    focused = int(request.args.get('focused'))
    try:
        table = Table.query.get(table_id)
        if request.files:
            uploaded_file = request.files["filename"]
            uploaded_file.filename = 'data.csv'
            file_path = "app"+url_for('static', filename="uploads/")+uploaded_file.filename
            uploaded_file.save(file_path)
            for row in get_data(file_path):
                data=dict(zip(table.param_names.split('.'), row))
                add_record_str = """
for key, value in {**data,**{f"{table.formula_name}": """+table.formula_name+"""(**data)}}.items():
    create(Cell, db, {'key': key, 'value': value, 'table_id': table_id})"""
                script = table.script + "\n{}"
                exec(script.format((add_record_str)))
    except:
        flash("The format may not correspond. N column should be the same and should be csv format")
    if focused == 0:
        return redirect(url_for('.index', collection_id=collection_id))
    elif focused == 1:
        return redirect(url_for('.view_table', table_id=table_id, collection_id=collection_id))


@table.route('/view-table', methods=['GET', 'POST'])
def view_table():
    collection_id = int(request.args.get('collection_id'))
    collection = Collection.query.get(collection_id)
    table_id = int(request.args.get('table_id'))
    table = Table.query.get(table_id)
    return render_template("table/table.html", table=table, collection=collection, focus=1)

@table.route('/show-chart')
def show_chart():
    column_name = str(request.args.get('column_name'))
    table_id = int(request.args.get('table_id'))
    table = Table.query.get(table_id)
    cells_list = []
    cells = list(Cell.query.filter_by(table_id=table_id).filter_by(key=column_name).all())
    for cell in cells:
        cells_list.append(cell.value)
    return render_template("table/charts/cell_chart.html", table=table, data=cells_list, column_name=column_name)
