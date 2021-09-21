import os

def titlebarThing():
    os.system('clear')

    print('******************')
    print('*** Calculator ***')
    print('******************\n')

def mainMenu():
    print("\nFormula: ")
    print("[1] Basic")
    print("[2] Advanced")
    print("[3] Scientific")
    print("[q] Quit")
    return input("Option: ")

def basicMenu():
    print("\n[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    return input("Option: ")

def advancedMenu():
    print("\n[1] Area Menu")
    print("[2] Mass Menu")
    print("[3] Volume")
    # print("[4]")
    return input("Option: ")

def scientificMenu():
    print("\n[1] Ro")
    print("[2] Pressure (F/A)")
    print("[3] Pressure (pgh)")
    #print("[4]")
    return input("Option: ")

def areaMenu():
	print("\n Area of: ")
	print("[1] Triangle")
	print("[2] Trapezoid")
	print("[3] Parallelogram")
	print("[4] Circle")
	print("[5] Square")
	return input("Option: ")

def massMenu():
	print("\n Mass Obtained from:")
	print("[1] Density and Volume")
	print("[2] Weight")
	print("[3] Force")
	print("[4] Energy")
	return input("Option: ")

def printAnswer(z):
    print("Answer is: " + str(z))
    input("[ENTER]")
    titlebarThing()