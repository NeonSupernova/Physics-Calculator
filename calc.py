import PySimpleGUI as sG

pi = 3.14159
g = 9.80
c = 299792458
zero = -273.15


def user_has(item=None):
    a = input("Do you have the " + item + "? (Y/N)")
    match a:
        case "y":
            return True
        case "Y":
            return True
        case "n":
            return False
        case "N":
            return False


def ro(infunc=False):
    if infunc == True:
        return float(input("Enter ro"))
    else:
        return massMenu() * volume()


def volume(infunc=False):
    if infunc == True:
        return float(input("Enter Volume:"))
    else:
        return float((areaMenu(userHas("Area")) * float(input("Enter Height: "))))


### Area Functions ###
def areaTriangle():
    return (float(input("Base: ")) * float(input("Height: ")) / 2)


def areaTrapezoid():
    h, b1, b2 = (
        float(input("Height: ")),
        float(input("Base 1: ")),
        float(input("Base 2: ")),
    )
    return (h * (b1 + b2)) / 2


def areaParallelogram():
    return float(input("Base: ")) * float(input("Height: "))


def areaCircle():
    r = float(input('Radius: '))
    return (float((r * r) * pi))


def areaSquare():
    return float(input("Width: ")) * float(input("Height: "))


### End Area ###
### Mass Functions ###
def massPV():
    return (float((ro(userHas("Ro")) * volume(userHas("volume")))))


def massWG():
    return ((float(input("Enter Weight: "))) / g)


def massFA():
    return ((float(input("Enter Force: ")) / g))


def massEC():
    return ((float(input("Enter Energy: ")) / g))


### End Mass ###
### Pressure ###
def pressureFA():
    return (float(input("Enter Force")) / areaMenu(userHas("")))


def pressurePGH():
    return ((ro() * float(input("Enter Height: "))))


def areaMenu(infunc=False):
    if infunc == True:
        return float(input("Area: "))
    print("\n Area of: ")
    print("[1] Triangle")
    print("[2] Trapezoid")
    print("[3] Parallelogram")
    print("[4] Circle")
    print("[5] Square")
    choice = int(input("Option: "))
    match choice:
        case 1:
            return areaTriangle()
        case 2:
            return areaTrapezoid()
        case 3:
            return areaParallelogram()
        case 4:
            return areaCircle()
        case 5:
            return areaSquare()


def massMenu(infunc=False):
    if infunc == True:
        return float(input("Area: "))
    print("\n Mass Obtained from:")
    print("[1] Density and Volume")
    print("[2] Weight")
    print("[3] Force")
    print("[4] Energy")
    choice = int(input("Option: "))
    match choice:
        case 1:
            return massPV()
        case 2:
            return massWG()
        case 3:
            return massFA()
        case 4:
            return massEC()


def pressureMenu(infunc=False):
    if infunc:
        return float(input("Pressure: "))
    print("[1] Pressure from Force and Area")
    print("[2] Pressure from Ro and Height")
    choice = int(input("Option:"))
    match choice:
        case 1:
            return pressureFA()
        case 2:
            return pressurePGH()


### End Pressure ###

def term():
    import os

    def titlebarThing():
        os.system("clear")

        print("******************")
        print("*** Calculator ***")
        print("******************")
        print("v0.4.1\n")

    def menu():
        print("\n[1] Area Menu")
        print("[2] Mass Menu")
        print("[3] Add")
        print("[4] Subtract")
        print("[5] Multiply")
        print("[6] Divide")
        print("[7] Volume")
        print("[8] Ro")
        print("[9] Pressure (F/A)")
        print("[10] Pressure (pgh)")
        print("[q] Quit")
        return input("Option: ")

    def printAnswer(z):
        print("Answer is: " + str(z))
        input("[ENTER]")
        titlebarThing()

    ### End Menus ###
    ### Program ###
    titlebarThing()
    choice = ""

    while choice != "q":

        choice = menu()
        titlebarThing()
        match choice:
            case "1":
                printAnswer(areaMenu())
            case "2":
                printAnswer(massMenu())
            case "3":
                printAnswer(float(input("Addend 1: ")) + float(input("Addend 2: ")))
            case "4":
                printAnswer(float(input("Minuend: ")) - float(input("Subtrahend")))
            case "5":
                printAnswer(float(input("Factor 1: ")) * float(input("Factor 2: ")))
            case "6":
                printAnswer(float(input("Dividend: ")) + float(input("Divisor: ")))
            case "7":
                printAnswer(volume())
            case "8":
                printAnswer(ro(massMenu(), volume()))
            case "9":
                printAnswer(pressureFA())
            case "10":
                printAnswer(pressurePGH())
            case "q":
                print("Thanks for using a Calculator")
                exit()
            case _:
                print("I did not understand input. Try again")


sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Button('Add'), sg.ButtonMenu('Area')],
          [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    window.close()

useTerm = False
#################

if useTerm == True:
    term()
else:
    gui()
