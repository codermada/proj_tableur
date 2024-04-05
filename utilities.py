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