from functions.Menu import Menu
from functions.utils import multi_numeric_input


def volume():
    area, height = multi_numeric_input('area', 'height')
    return area * height


def density():
    mass, vol = multi_numeric_input("mass", "volume")
    return mass / volume()


VolumeMenu = Menu(
    "Area Menu", "Select an option from the Menu", [
        volume,
        density
    ]
)

