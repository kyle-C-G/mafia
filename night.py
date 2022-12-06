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
        player.nightAction(playerClass=p)

def getMafiaVoted(playerlist: list[p]) -> p:
    highestVotedPlayer = {"votes": 0, "player": p}
    for player in playerlist:
        if player.getMafiaVoteCount() > highestVotedPlayer["votes"]:
            highestVotedPlayer["player"]: p = player
    return highestVotedPlayer["player"]

def resetPlayers(playerList: list[p]) -> None:
    player: p
    for player in playerList:
        player.nightReset()

def night(count: int) -> None:
    playerActions(count=count, playerList=p.alivePlayerList)
    votedPlayer: p = getMafiaVoted(playerlist=p.alivePlayerList)
    os.system("cls")
    votedPlayer.kill()
    resetPlayers(playerList=p.alivePlayerList)

def doActions(playerList: list[p]) -> None:
    getMafiaVoted(playerlist = playerList)

def checks() -> None:
    return

def night(dayCount: int) -> None:
    playerList = p.alivePlayerList
    playerActions(count = dayCount, playerList = playerList)
    checks()
    doActions(playerlist = playerList)
    resetPlayers()
    return
