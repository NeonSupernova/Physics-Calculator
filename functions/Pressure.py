from functions.Menu import Menu
from functions.utils import multi_numeric_input


def pressureFA():
    force, area = multi_numeric_input('force', 'area')
    return force * area


def pressurePGH():
    x, y = multi_numeric_input('density', 'height')
    return x * y


PressureMenu = Menu(
    "Pressure Menu", "Select an option from the Menu", [
        pressurePGH,
        pressureFA
    ]
)
