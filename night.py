import inquirer
import os
from player import Player as p

def playerActions(count: int, playerList: list[p]) -> None:
    player: p
    for player in playerList:
        os.system("cls")
        print(f"{player.getName()}'s turn:\n")
        player.passwordCheck()
        print(f"Night {count}:\n")
        player.nightPrompt(playerclass= p)

def resetPlayers(playerList: list[p]) -> None:
    player: p
    for player in playerList:
        player.nightReset()

def doAction(playerlist: list[p]) -> None:
    docList: list[p] = []
    mafiaList: list[p] = []
    investList: list[p] = []
    godList: list[p] = []
    townList: list[p] = []
    for player in playerlist:
        match player.getRoleName():
            case "Doctor":
                docList.append(player)
            case "Mafia":
                mafiaList.append(player)
            case "Investigator":
                investList.append(player)
            case "Godfather":
                godList.append(player)
            case "Town":
                townList.append(player)
    for doctor in docList:
        doctor.nightAction(playerClass = p)
    mafia = mafiaList[0]
    mafia.nightAction(playerClass = p)
    for invest in investList:
        invest.nightAction(playerClass = p)
    for godfather in godList:
        godfather.nightAction(playerClass = p)
    for town in townList:
        town.nightAction(playerClass = p)
    

def night(dayCount: int) -> None:
    playerList = p.alivePlayerList
    playerActions(count = dayCount, playerList = playerList)
    doAction(playerlist = playerList)
    resetPlayers(playerList=playerList)
    return
