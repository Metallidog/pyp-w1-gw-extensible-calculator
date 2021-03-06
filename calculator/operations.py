from functools import reduce

def add(*args):
    return sum(args)

def subtract(*args):
    return args[0] + -1*add(*args[1:])

def multiply(*args):
    return reduce(lambda a,b: a*b, args) if args else 0

def divide(*args):
    if args:
        if len(args)>1:
            return float(args[0]) / multiply(*args[1:])
        else:
            return args[0]
    else:
        return 0
        
