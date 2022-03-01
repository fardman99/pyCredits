import json
from os.path import *
import os

data = [] 
passes = [4, 4, True, 3, 3, True, True, 1, 6]

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
                if not x in ["Yes", "No"]:
                    raise ValueError("Not Yes or No")
                else:
                    if x == "Yes":
                        return True
                    if x == "No":
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
    
    if exists("creds.txt"): os.remove("creds.txt")
    
    with open("creds.txt", "w") as outfile:
        json.dump(data, outfile)

def loadData(): 
    global data
    with open("creds.txt", "r") as infile:
        data = json.load(infile)

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
    if not checkState(7):
        print("\n Art - 1")
    if not checkState(8):
        print("\nElectives - %d" % (passes[8] - data[8]))
    print("\n--Course Requirements--")
    if not checkState(2):
        print("\nAlgebra 2")
    if not checkState(5):
        print("\nHealth")
    if not checkState(6):
        print("\nPE")

def menu():
    print("---pyCredits---\nEnglish - %d Credits\nMath - %d Credits\nHistory - %d Credits\nScience - %d Credits\nArt - %d Credits\nElectives - %d Credits" % (data[0], data[1], data[3], data[4], data[7], data[8]))

    if data[0] < 4 or data[1] < 4 or data[2] != True or data[3] < 3 or data[4] < 3 or data[5] != True or data[6] != True or data[7] < 1 or data[8] < 6:
        prepareInfo()

    a = input("\nSetup or Quit? ")
    if a == "Setup":
        clear()
        setup()
        menu()
    elif a == "Quit":
        clear()
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
    
def main():
    global data
    clear()
    if exists("creds.txt"): loadData()
    else: setup()
    menu()
    
if __name__ == "__main__": main()