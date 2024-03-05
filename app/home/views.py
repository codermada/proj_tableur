from flask import render_template, redirect, url_for, request

from . import home
from .forms import CellForm

from .. import db
from ..models import Column, Row, Cell

@home.route('/', methods=['GET', 'POST'])
def index():
    row_forms = []
    rows = Row.query.all()
    n_max_col = 1
    if len(list(rows)) > 0:
        for row in rows:
            col_forms = []
            if n_max_col < len(list(row.columns)):
                n_max_col = len(list(row.columns))
            row.set_i(list(rows).index(row))
            db.session.add(row)
            db.session.commit()
            if len(list(row.columns)) > 0:
                for col in row.columns:
                    col.set_j(list(row.columns).index(col))
                    db.session.add(col)
                    db.session.commit()
                    for cel in col.cells:
                        cel.set_i(list(rows).index(row))
                        cel.set_j(list(row.columns).index(col))
                        db.session.add(cel)
                        db.session.commit()
                        col_forms.append(CellForm(f'({cel.i}, {cel.j})'))
                row_forms.append(col_forms)
        for row in rows:
            row.n_max_col = n_max_col
            db.session.add(row)
            db.session.commit()
    return render_template('home/index.html', row_forms=row_forms, rows=rows, n_max_col=n_max_col)

@home.route('/add-row', methods=['GET', 'POST'])
def add_row():
    n_max_col = int(request.args['n_max_col'])
    row = Row()
    db.session.add(row)
    db.session.commit()
    for i in range(0, n_max_col):
        column = Column()
        row.columns.append(column)
        db.session.add(row)
        cell = Cell()
        db.session.add(cell)
        column.cells.append(cell)
        db.session.add(column)
        db.session.commit()
    return redirect(url_for('.index'))

@home.route('/delete-row', methods=['GET', 'POST'])
def delete_row():
    return redirect(url_for('.index'))

@home.route('/add-column', methods=['GET', 'POST'])
def add_column():
    n_max_col = int(request.args['n_max_col']) + 1
    rows = Row.query.all()
    for row in list(rows):
        n_col = len(list(row.columns))
        if n_col < n_max_col:        
            column = Column()
            row.columns.append(column)
            db.session.add(row)
            cell = Cell()
            db.session.add(cell)
            column.cells.append(cell)
            db.session.add(column)
            db.session.commit()
            n_col += 1
    return redirect(url_for('.index'))

@home.route('/delete-column', methods=['GET', 'POST'])
def delete_column():
    return redirect(url_for('.index'))

# @home.route('/', methods=['GET', 'POST'])
# def ():
#     return 

@home.route('/populate-cell', methods=['GET', 'POST'])
def populate_cell():
    cell_id = int(request.args['id'])
    return redirect(url_for('.index'))