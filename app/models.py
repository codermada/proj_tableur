from . import db
from .db_operations import create, delete

import os

path = os.path.join(os.path.curdir,"app/formulas.data.py")

with open(path, 'r') as file:
    formulas = file.read().split("#")


class Formula(db.Model):
    __tablename__ = 'formulas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    kind = db.Column(db.String(500), default="general")
    script = db.Column(db.Text, default="")
    def __repr__(self):
        return f'<Formula {self.id}>'
    @staticmethod
    def generate():
        for (name, script) in list(zip(formulas[0].strip("\n").split('.'), formulas[1:])):
            create(Formula, db, {'name': name, 'script': script})
    @staticmethod
    def delete_all():
        for formula in Formula.query.filter_by(kind='general').all():
            delete(Formula, db, formula.id)
    @staticmethod
    def update():
        Formula.delete_all()
        Formula.generate()

class Collection(db.Model):
    __tablename__ = 'collections'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), default=f"collection_{str(id)}")
    tables = db.relationship('Table', backref='collection', lazy='dynamic', cascade="all, delete-orphan")
    def __repr__(self):
        return f'<Collection {self.id}>'

class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), default="tables")
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'))
    formula_name = db.Column(db.String(500), default="")
    param_names = db.Column(db.String(5000), default="")
    script = db.Column(db.Text, default="")
    n_col = db.Column(db.Integer, default=0)
    cells = db.relationship('Cell', backref='table', lazy='dynamic', cascade="all, delete-orphan")
    def __repr__(self):
        return f'<Table {self.id}>'

class Cell(db.Model):
    __tablename__ = 'cells'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(500), default="")
    value = db.Column(db.Float, default=0)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'))
    def __repr__(self):
        return f'<Cell {self.id}>'
    @staticmethod
    def get_last_result(table_id, n_col):
        table = Table.query.get(table_id)
        from api.resources import to2D, reverse
        cell_list = []
        cells = list(table.cells.filter_by(table_id=table_id))
        for cell in cells:
            cell_list.append(cell.value)
        cell_list = reverse(to2D(cell_list, n_col))
        return cell_list[0][n_col-1]