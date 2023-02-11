from functions.utils import multi_numeric_input
from functions.Menu import Menu
from math import pi, pow


def areaTriangle():
    base, height = multi_numeric_input('base', 'height')
    return (base * height) / 2


def areaTrapezoid():
    h, b1, b2 = multi_numeric_input('height', 'base 1', 'base 2')
    return (h * (b1 + b2)) / 2


def areaParallelogram():
    base, height = multi_numeric_input('base', 'height')
    return base * height


def areaCircle():
    r = multi_numeric_input('radius')[0]
    return pow(r, 2) * pi


def areaSquare():
    width, height = multi_numeric_input('width', 'height')
    return width * height


AreaMenu = Menu(
    "Area Menu", "Select an option from the Menu", [
        areaTriangle,
        areaSquare,
        areaCircle,
        areaParallelogram,
        areaTrapezoid
    ]
)
