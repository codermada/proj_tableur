from flask import render_template, redirect, request, url_for, flash

from . import formula

from .. import db
from ..models import Collection, Table, Formula, Cell
from ..db_operations import create, update, delete

@formula.route('/')
def index():
    formulas_general = Formula.query.filter_by(kind='general').all()
    formulas_custom = Formula.query.filter_by(kind='custom').all()
    return render_template('formula/index.html', formulas_general=formulas_general, formulas_custom=formulas_custom)

@formula.route('/create-formula', methods=['post', 'get'])
def create_formula():
    if request.method == 'POST':
        create(Formula, db, {'name': request.form.get('name'), 'kind': 'custom'})
        return redirect(url_for('.index'))
    return redirect(url_for('.index'))

@formula.route('/delete-formula', methods=['post', 'get'])
def delete_formula():
    formula_id = int(request.args.get('formula_id'))
    delete(Formula, db, formula_id)
    return redirect(url_for('.index'))

@formula.route('/add-script', methods=['post', 'get'])
def add_script():
    formula_id = int(request.args.get('formula_id'))
    if request.method == 'POST':
        update(Formula, db, {'script': request.form.get('script')}, formula_id)
        return redirect(url_for('.index'))
    return redirect(url_for('.index'))

@formula.route('/same-formula-chart')
def same_formula_chart():
    formula_name = str(request.args.get('formula_name'))
    tables = list(Table.query.filter_by(formula_name=formula_name).all())
    categories = []
    values = []
    try:
        for table in tables:
            values.append(table.cells[0].get_last_result(table.id, table.n_col + 1))
            categories.append(table.name)
        return render_template("formula/charts/same_formula_chart.html", categories=list(categories), values=values, formula_name=formula_name)
    except:
        flash("A table using the formula is empty")
        return redirect(url_for(".index"))