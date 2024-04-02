# exec(f"""
# def add(*args):
#     #result = 0
#     #for i in args:
#     #    result = result + i
#     return args[0] + (args[1] + args[2]) * {3}

# x = add(1, 1, 1)""")
# print(x)


# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# def add_(**kargs):
#     sum = kargs['A'] + kargs['B']
#     return sum

# print(add(1, 3, 4, 5))
# print(add_(A=1, B=2))
# exec("""
# print(add_({}))
# """.format("A=2, B=3")
# )

# def add(a, b, d=12):
#     return a+b+d

# import inspect

# print(inspect.signature(add), add.__name__)
# print(len(list(inspect.signature(add).parameters.values())))
# print(list(inspect.signature(add).parameters.values())[2].name)
# print(list(inspect.signature(add).parameters.values())[1].default)

# print('.'.join(["q", "w"]).split(sep='.'))

print({**{'a':1},**{'b':2}}, 1)
