from flask import request

from flask_restful import Resource

from app.models import Formula, Table, Cell

def to2D(the_list, n_col):
    result = []
    row = []
    j = 0
    n_col = int(n_col)
    for element in the_list:
        row.append(element)
        j += 1
        if j == n_col:
            result.append(row)
            row = []
            j = 0
    return result

def reverse(the_list):
    result = the_list[::-1]
    return result

class TableResource(Resource):
    def get(self):
        table_id = int(request.args.get('table_id'))
        table = Table.query.get(table_id)
        cells = []
        for cell in list(table.cells):
            cells.append(cell.value)
        cells = to2D(cells, table.n_col + 1)
        cells = reverse(cells)
        return cells


class CellResource(Resource):
    def get(self):
        column_name = str(request.args.get('column_name'))
        table_id = int(request.args.get('table_id'))
        table = Table.query.get(table_id)
        cells_list = []
        cells = list(Cell.query.filter_by(table_id=table_id).filter_by(key=column_name).all())
        for cell in cells:
            cells_list.append(cell.value)
        # cells_list = reverse(cells_list)
        return cells_list