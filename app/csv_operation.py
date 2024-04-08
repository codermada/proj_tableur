import csv
from utilities import to2D, reverse
def get_data(path):
    data = []
    result = []
    with open(path) as file:
        csv_file=csv.reader(file)
        for row in csv_file:
            data.append(row)
    for row in data:
        n_col = len(row)
        for j in row:
            result.append(j)
    return reverse(to2D(result, n_col))
