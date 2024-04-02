import inspect

def nb_params(func):
    return len(list(inspect.signature(func).parameters.values()))

def params(func):
    return list(inspect.signature(func).parameters.values())

def param_names(func):
    n = nb_params(func)
    param_names = []
    for i in range(n):
        param_names.append(list(inspect.signature(func).parameters.values())[i].name)
    return '.'.join(param_names)

