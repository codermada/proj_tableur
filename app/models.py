from . import db


table = db.Table(
    'table',
    db.Column('cell_id', db.Integer, db.ForeignKey('cells.id')),
    db.Column('row_id', db.Integer, db.ForeignKey('rows.id')),
    db.Column('column_id', db.Integer, db.ForeignKey('columns.id'))
)


class Cell(db.Model):
    __tablename__ = 'cells'
    id = db.Column(db.Integer, primary_key=True)
    i = db.Column(db.Integer, default=0)
    j = db.Column(db.Integer, default=0)
    k = db.Column(db.Integer, default=0)
    value = db.Column(db.Float, default=0.0)
    def __repr__(self):
        return f'<cell {self.id}>'
    def set_i(self, i):
        self.i = i
    def set_j(self, j):
        self.j = j


class Column(db.Model):
    __tablename__ = 'columns'
    id = db.Column(db.Integer, primary_key=True)
    j = db.Column(db.Integer, default=0)
    cells = db.relationship('Cell', 
                             secondary=table,
                             backref=db.backref('columns', lazy='dynamic'),
                             lazy='dynamic')
    def __repr__(self):
        return f'<column {self.id}>'
    def set_j(self, j):
        self.j = j


class Row(db.Model):
    __tablename__ = 'rows'
    id = db.Column(db.Integer, primary_key=True)
    i = db.Column(db.Integer, default=0)
    n_max_col = db.Column(db.Integer, default=1)
    columns = db.relationship('Column', 
                             secondary=table,
                             backref=db.backref('rows', lazy='dynamic'),
                             lazy='dynamic')
    def __repr__(self):
        return f'<row {self.id}>'
    def set_i(self, i):
        self.i = i
