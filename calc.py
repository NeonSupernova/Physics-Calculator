import os
from basics import *
from area import *
from mass import *
from menus import *
from pressure import *

### Mathematical Functions ###
    
    ### Advanced ###

def volume(area, height):
    V = multiply(area, height)
    return V

    ### Scientific ###

def ro(mass, vol):
    ro = divide(mass, vol)
    return ro

### Other Functions ###

def areaChoice():
    try:
        have = input("Do you have the area? y/n: ")
        if have == 'n':
            squareorcircle = input("[s] Square\n[c] Circle\n")
            if squareorcircle == 's':
                x, y = input("Width:"), input("Length: ")
                x = areaSquare(float(x), float(y))
            elif squareorcircle == 'c':
                x = input("Radius: ")
                x = areaCircle(float(x))
        elif have == 'y':
                x = input("Area :")
        return x
    except: Exception in e
    print(e)

def volChoice():
    try:
        have = input("Do you have volume? y/n:\n")
        if have == 'n':
            x, y = areaChoice(), input("Height:")
            z = volume(float(x), float(y))    
        elif have == 'y':
            z = input("Volume :")
        return x
    except: Exception in e
    print(e)
def massChoice():
    try:
        have = input("Do you have the mass? y/n\n")
        if have == 'n':
            choice3 = massMenu()
            if choice3 == '1':
                x, y = input("Density: "), volChoice()
                z = massPV(float(x), float(y))
            elif choice3 == '2':
                x = input("Weight: ")
                z = massWG(float(x))
           elif choice3 == '3':
                x = input("Force")
                z = massFA(float(x))
            elif choice3 == '4':
                x = input("Energy: ")
                z = massEC(float(x))
        elif have == 'y':
            z = input("Enter Area: ")
        return z
    except: Exception in e
    print(e)
    
### Program ###


titlebarThing()
choice = ''

while choice != 'q':

    choice = mainMenu()
    titlebarThing()
    if choice == '1':
        choice2 = basicMenu()
        titlebarThing()
        if choice2 == '1':
            x, y = input("Addend 1: "), input("Addend 2:")
            z = add(float(x), float(y))
            printAnswer(z)
        elif choice2 == '2':
            x, y = input("Minuend: "), input("Subtrahend")
            z = subtract(float(x), float(y))
            printAnswer(z)
        elif choice2 == '3':
            x, y = input("Factor 1: "), input("Factor 2:")
            z = multiply(float(x), float(y))
            printAnswer(z)
        elif choice2 == '4':
            x, y = input("Dividend: "), input("Divisor:")
            z = divide(float(x), float(y))
            printAnswer(z)

    elif choice == '2':
        choice2 = advancedMenu()
        titlebarThing()
        if choice2 == '1':
            choice3 = areaMenu() 
            titlebarThing()
            if choice3 == '1':
                x, y = input("Base: "), input("Height: ")
                z = areaTriangle(float(x), float(y))
                printAnswer(z)
            elif choice3 == '2':
                w, x, y = input("Height: "), input("Base 1: "), input("Base2")
                z = areaTrapezoid(float(w), float(x), float(y))
                printAnswer(z)
            elif choice3 == '3':
                x, y = input("Base: "), input("Height")
                z = areaParallelogram(float(x), float(y))
                printAnswer(z)
            elif choice3 == '4':
                x = input("Radius: ")
                z = areaCircle(float(x))
                printAnswer(z)
            elif choice3 == '5':
                x, y = input("Base: "), input("Length: ")
                z = areaSquare(float(x),float(y))
                printAnswer(z)
        elif choice2 == '2':
            choice3 = massMenu()
            titlebarThing()
            if choice3 == '1':
                x, y = input("Density: "), volChoice()
                z = massPV(float(x), float(y))
                printAnswer(z)
            elif choice3 == '2':
                x = input("Weight: ")
                z = massWG(float(x))
                printAnswer(z)
            elif choice3 == '3':
                x = input("Force")
                z = massFA(float(x))
                printAnswer(z)
            elif choice3 == '4':
                x = input("Energy: ")
                z = massEC(float(x))
                printAnswer(z)
        elif choice2 == '3': 
            x, y = areaChoice(), input("Height:")
            z = volume(float(x), float(y))
            printAnswer(z)

    elif choice == '3':
        choice2 = scientificMenu()
        titlebarThing()
        if choice2 == '1':
            x, y = massChoice(), volChoice()
            z = ro(float(x), float(y))
            printAnswer(z)
        elif choice2 == '2':
            x, y = input("Force: "), areaChoice()
            z = pressureFA(float(x), float(y))
            printAnswer(z)
        elif choice2 == '3':
            x, y = input("Ro: "), input("Height")
            z = pressurePGH(float(x), float(y))
            printAnswer(z)

    elif choice == 'q':
        print("Thanks for using a Calculator")
        exit()
    else:
        print("I did not understand input. Try again")