import inquirer
from player import Player
import os

os.system("cls")

def addPlayer(count) -> None:
    os.system("cls")
    print(f"Player {count}")
    nameVerification: bool = True
    passwordVerification: bool = True
    # options = ["Town", "Mafia", "Doctor", "Investigator", "Godfather"]
    # options: list[str] = ["town", "mafia", "doctor", "investigator", "godfather"]
    questions = [ 
        inquirer.List("Role", 
            message="Pick a Role", 
            choices=["Mafia", "Godfather", "Town", "Doctor", "Investigator"])]
    while nameVerification:
        name: str = input("Enter your name:\n")
        if name == "" or name == " " or name == None:
            print("Name is too short\n")
        elif len(name) < 15:
            nameVerification = False
            break
        else:
            print("Name is too long.\n")
    while passwordVerification:
        password: str = input("Enter a password:\n")
        if len(password) > 1:
            passwordVerification = False
            break
        else:
            print("Password needs to be longer.\n")
    answers = inquirer.prompt(questions)
    print(answers["Role"])
    Player(name=name, role=answers["Role"], password=password)
    return

def numberPlayers() -> int:
    os.system("cls")
    numberVerification: bool = True
    while numberVerification:
        try:
            number: int = int(input("How many people are playing?\n"))
        except:
            print("That was not a number.\n")
        if number > 0:
            numberVerification = False
        else:
            print("Number needs to be greater than zero.\n")
        
    return number

def createXPlayers() -> None:
    X = numberPlayers()
    count = 1
    for each in range(0, X):
        addPlayer(count=count)
        count += 1
    return
        
