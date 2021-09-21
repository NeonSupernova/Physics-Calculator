from basics import *

def massPV(p, v):
	M = multiply(p, v)
	return M

def massWG(w):
	M = multiply(w, g)
	return M

def massFA(f):
	M = divide(f, g)
	return M 

def massEC(e):
	M = divide(e, c)
	return M
