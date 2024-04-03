from flask import render_template, redirect, request, url_for

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
