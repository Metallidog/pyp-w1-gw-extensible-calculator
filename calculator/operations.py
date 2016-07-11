from functools import reduce

def add(*args):
    if validate(args):
        return sum(args)
    else:
        raise InvalidParams

def subtract(*args):
    return args[0] + -1*add(*args[1:])

def multiply(*args):
    if args:
        return reduce(lambda a,b: a*b, args) 
    else:
        return 0

def divide(*args):
    if args:
        if len(args)>1:
            return float(args[0]) / multiply(*args[1:])
        else:
            return args[0]
    else:
        return 0

def validate(args):
    if any(isinstance(a, str) for a in args):
        return False
    else:
        return True
