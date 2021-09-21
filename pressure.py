from basics import *

def pressureFA(force, area):
    P = divide(force, area)
    return P

def pressurePGH(ro, h):
    x = multiply(ro, h)
    P = multiply(x, g)
    return P