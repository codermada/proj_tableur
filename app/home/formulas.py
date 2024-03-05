def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum 

# def add_(**kargs):
#     sum = kargs['A'] + kargs['B']
#     return sum

# print(add(1, 3, 4, 5))
# print(add_(A=1, B=2))
# exec("""
# print(add_({}))
# """.format("A=2, B=3")
# )

def add(a, b, d):
    return a+b+d

import inspect

print(len(list(inspect.signature(add).parameters.values())))