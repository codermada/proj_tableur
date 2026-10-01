def add(*args):
    result = 0
    for e in args:
        result = result + float(e)
    return result

def substract(a, b):
    return float(a) - float(b)

def divide(a, b):
    return float(a) / float(b)

def multiply(a, b):
    return float(a) * float(b)