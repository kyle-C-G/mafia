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

def getHighestVoted(playerlist: list[p]) -> p:
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
    votedPlayer: p = getHighestVoted(playerlist=p.alivePlayerList)
    os.system("cls")
    votedPlayer.kill()
    resetPlayers(playerList=p.alivePlayerList)

