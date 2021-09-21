from basics import *

def areaTriangle(b, h):
	A = divide(multiply(b, h), 2)
	return A

def areaTrapezoid(h, b1, b2):
	x = add(b1, b2)
	A = divide(multiply(h, x), 2)
	return A

def areaParallelogram(b, h):
	A = multiply(b, h)
	return A

def areaCircle(radius):
    sqrR = multiply(radius, radius)
    area = multiply(sqrR, pi)
    return area

def areaSquare(w, l):
    area = multiply(w, l)
    return area