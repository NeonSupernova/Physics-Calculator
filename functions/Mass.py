from functions.Menu import Menu
from functions.utils import CONSTANTS, multi_numeric_input


def massPV():
    d, v = multi_numeric_input('density', 'volume')
    return d * v


def massWG():
    return multi_numeric_input('weight')[0] / CONSTANTS['gravity']


def massFA():
    return multi_numeric_input('force')[0] / CONSTANTS['gravity']


def massEC():
    return multi_numeric_input('energy')[0] / CONSTANTS['gravity']


MassMenu = Menu(
    "Mass Menu", "Select an option from the Menu", [
        massEC,
        massFA,
        massWG,
        massPV
    ]
)
