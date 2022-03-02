from os.path import *
import os, sys, json
from tabnanny import check
from tkinter import W

data = [] 
passes = [4, 4, True, 3, 3, True, True, 1, 6]
path = "creds.txt"
x = float()

def getInt():
    for i in range(100):
        while True:
            try:
                 return int(input())
            except: 
                print("Invalid input.")
                continue
            break

def getBool():
    for i in range(100):
        while True:
            try:
                x = input()
                if not x in ["Yes", "No", "yes", "no", "y", "n", "Y", "N"]:
                    raise ValueError("Not Yes or No")
                else:
                    if x in ["Yes", "yes", "y", "Y"]:
                        return True
                    if x in ["No", "no", "n", "N"]:
                        return False
            except:
                print("Invalid input.")
                continue
            break
                
def setup():
    global data
    data = []
    print("--Setup--\n\nHow many English credits do you currently have?")
    data.append(getInt())
    print("How many Math credits do you have?")
    data.append(getInt())
    print("Have you passed Algebra 2 (Yes/No)")
    data.append(getBool())
    print("How many History credits do you have?")
    data.append(getInt())
    print("How many Science credits do you have?")
    data.append(getInt())
    print("Do you have your 1/2 Health credit?")
    data.append(getBool())
    print("Do you have your 1/2 PE credit?")
    data.append(getBool())
    print("How many Art credits do you have?")
    data.append(getInt())
    print("How many Elective credits do you have?")
    data.append(getInt())
    print("Setup complete.")

    clear()
    saveData()
    
def saveData():
    global data
    try:
        if exists(path): os.remove(path)
    except:
        print("Error removing %s" % (path))
        exit()
    
    try:
        with open(path, "w") as outfile:
            json.dump(data, outfile)
    except:
        print("Error saving %s" % (path))

def loadData(): 
    global data
    try:
        with open(path, "r") as infile:
            data = json.load(infile)
    except:
        print("Error loading %s" % (path))
        exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkState(x):
    if x in [0, 1, 3, 4, 7, 8]:
        if data[x] < passes[x]:
            return False
        else: return True
    else:
        if data[x] != True:
            return False
        else: return True

def prepareInfo():
    global x
    print("\n--Credits needed--")
    if not checkState(0):
        print("\nEnglish - %d" % (passes[0] - data[0]))
    if not checkState(1):
        print("\nMath - %d" % (passes[1] - data[1]))
    if not checkState(3):
        print("\nHistory - %d" % (passes[3] - data[3]))
    if not checkState(4):
        print("\nScience - %d" % (passes[4] - data[4]))
    if not checkState(5):
        print("\nHealth - 0.5")
    if not checkState(6):
        print("\nPE - 0.5")
    if not checkState(7):
        print("\nArt - 1")
    if not checkState(8):
        print("\nElectives - %d" % (passes[8] - data[8]))
    if getTotal() != 23.0:
        print("\nTotal - %0.1f" % (23.0 - x))
    if not checkState(2):
        print("\nYou must also pass Algebra 2.")

def getTotal():
    global x
    x = float(data[0] + data[1] + data[3] + data[4] + data[7] + data[8])
    if data[5]:
        x = x + 0.5
    if data[6]:
        x = x + 0.5

def printTotal():
    print("Total -  %0.1f" % (x))
    if x >= 23.0 and data[2] and data[5] and data[6]:
        print("You meet the credit and class requirements for graduation.")
    if x < 23.0:
        print("You need %0.1f more credit(s) to meet the requirements." % (23.0 - x))
    return x

def menu():
    print("---pyCredits---\nEnglish - %d Credits\nMath - %d Credits\nHistory - %d Credits\nScience - %d Credits\nArt - %d Credits\nElectives - %d Credits" % (data[0], data[1], data[3], data[4], data[7], data[8]))
    if data[5]: print("PE - 0.5 Credits")
    else: print("PE - 0 Credits")
    if data[6]: print("Health - 0.5 Credits")
    else: print("Heatlh - 0 Credits")

    getTotal()
    printTotal()
    
    if data[0] < 4 or data[1] < 4 or data[2] != True or data[3] < 3 or data[4] < 3 or data[5] != True or data[6] != True or data[7] < 1 or data[8] < 6:
        prepareInfo()

    a = input("\nSetup or Quit? ")
    if a in ["Setup", "setup", "s", "S"]:
        clear()
        setup()
        menu()
    elif a in ["Quit", "quit", "q", "Q"]:
        clear()
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
    
def main():
    global data
    clear()
    if exists(path): loadData()
    else: setup()
    menu()
    
if __name__ == "__main__":
    try: path = sys.argv[1]
    except: pass
    main()