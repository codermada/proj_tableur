from flask import request

from flask_restful import Resource

from app.models import Formula, Table, Cell

from utilities import to2D, reverse

class TableResource(Resource):
    def get(self):
        """usage
http://127.0.0.1:5000/api/table-cells?table_id=1
        """
        table_id = int(request.args.get('table_id'))
        table = Table.query.get(table_id)
        cells = []
        for cell in list(table.cells):
            cells.append(cell.value)
        cells = to2D(cells, table.n_col + 1)
        cells = reverse(cells)
        return cells


class CellColumnResource(Resource):
    def get(self):
        """usage
http://127.0.0.1:5000/api/table-column?table_id=1&column_name=name
        """
        column_name = str(request.args.get('column_name'))
        table_id = int(request.args.get('table_id'))
        table = Table.query.get(table_id)
        column_data = []
        cells = list(Cell.query.filter_by(table_id=table_id).filter_by(key=column_name).all())
        for cell in cells:
            column_data.append(cell.value)
        return column_data


class CellRowResource(Resource):
    def get(self):
        """usage
http://127.0.0.1:5000/api/table-row?table_id=3&row_id=2
        """
        row_id = int(request.args.get('row_id'))
        table_id = int(request.args.get('table_id'))
        table = Table.query.get(table_id)
        labels = table.param_names.split('.')
        labels.append(table.formula_name)
        row_data = []
        cells = list(Cell.query.filter_by(table_id=table_id).all())
        for cell in cells:
            row_data.append(cell.value)
        row_data = reverse(to2D(row_data, table.n_col + 1))[row_id]
        return dict(zip(labels, row_data))