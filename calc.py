from functions.Menu import Menu
from functions.Area import AreaMenu
from functions.Mass import MassMenu
from functions.Pressure import PressureMenu
from functions.Volume import VolumeMenu

mainMenu = Menu(
    "Main Menu", "Select an option from the Menu", [
        AreaMenu,
        MassMenu,
        PressureMenu,
        VolumeMenu
    ]
)

if __name__ == '__main__':
    mainMenu.run()
