import itertools

def bool_to_number(a : bool) -> int:
    return 1 if a else 0

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    x1 = AND(a, b)
    x2 = OR(a, b)
    x3 = NOT(x1)
    x4 = AND(x3, x2)
    return x4

def NAND(a, b):
    x1 = AND(a,b)
    x2 = NOT(x1)
    return x2

def NOR(a, b):
    x1 = OR(a, b)
    x2 = NOT(x1)
    return x2

def XNOR(a, b):
    x1 = XOR(a, b)
    x2 = NOT(x1)
    return x2

def HALF_ADDER(a, b):
    x1 = XOR(a, b)
    x2 = AND(a, b)
    return (x2, x1)

def FULL_ADDER(a, b):
    return

def LogicTable(func):
    func_vars = func.__code__.co_argcount
    combinations = list(itertools.product([True, False], repeat = func_vars))

    for i in combinations:
        print(i, '=', func(*i))




LogicTable(NAND)
