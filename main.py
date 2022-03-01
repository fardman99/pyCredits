import json
from os.path import *
import os

data = [] 

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

def checkPass(x):
    global data
    if data[x] == True:
        return "Yes"
    if data[x] == False:
        return "No"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("---pyCredits---\nEnglish - %d Credits\nMath - %d Credits\nHistory - %d Credits\nScience - %d Credits\nArt - %d Credits\nElectives - %d Credits" % (data[0], data[1], data[3], data[4], data[7], data[8]))
    print("\nAlgebra 2 passed? | %s" % (checkPass(2)))
    print("\nHealth passed? | %s" % checkPass(5))
    print("\nPE passed? | %s" % checkPass(6))

    a = input("Setup or Quit? ")
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
    
if __name__ == "__main__":
    main()