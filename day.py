import os
import time
from player import Player as p
import inquirer
import time

abstains: int = 0
votesFor: int = 0
votesAgainst: int = 0
player: p
playerFor: list[p] = []
playerAgainst: list[p] = []
playerAbstain: list[p] = []

def checkWon() -> str:
    mafia: int = 0
    town: int = 0
    for player in p.alivePlayerList:
        match player.getRoleName():
            case "Mafia":
                mafia += 1
            case "Town":
                town += 1
            case "Investigator":
                town += 1
            case "Doctor":
                town += 1
            case "Godfather":
                mafia += 1
    if mafia > town or (((town + mafia) == 2) and mafia == 1):
        return "Mafia Won."
    elif mafia == 0:
        return "Town Won."
    else:
        return "Game is not over."

def voteUp(alivePlayerNames, alivePlayers) -> p:
    os.system("cls")
    questions = [inquirer.List("VoteFor", 
        message="Select a person to stand trial", 
        choices=alivePlayerNames)]
    answers = inquirer.prompt(questions)
    votedPlayer: p = p.getPlayerByName(answers["VoteFor"])
    return votedPlayer

def voting(votedPlayer: p):
    for player in p.alivePlayerList:
        os.system("cls")
        if player == votedPlayer:
            pass
        else:
            print(f"{player.getName()}'s Turn:")
            player.passwordCheck()
            questions = [inquirer.List("PlayerVote", 
                message="Cast your vote", 
                choices=["For", "Against", "Abstain"])]
            answers = inquirer.prompt(questions)
            if answers["PlayerVote"] == "For":
                player.voteFor(player = votedPlayer)
                playerFor.append(player.getName())
            elif answers["PlayerVote"] == "Abstain":
                player.voteAbstain(player = votedPlayer)
                playerAbstain.append(player.getName())
            elif answers["PlayerVote"] == "Against":
                player.voteAgainst(player=votedPlayer)
                playerAgainst.append(player.getName())
    os.system("cls")
    if votedPlayer.lynchVotes["For"] > votedPlayer.lynchVotes["Against"]:
        time.sleep(2)
        input("Press enter to show results.")
        print(f"Players who voted for lynching {votedPlayer.getName()}:\n{', '.join(playerFor)}\n")
        print(f"Players who voted against lynching {votedPlayer.getName()}:\n{', '.join(playerAgainst)}\n")
        print(f"Players who abstained from voting:\n{', '.join(playerAbstain)}\n")
        votedPlayer.kill()
        time.sleep(10)
    else:
        print(f"{votedPlayer.getName()} was not lynched.")
        print("Day has ended.")
        time.sleep(2)

 
def day(dayCount: int) -> bool:
    players: list[p] = p.playerList
    playerCont: int = p.playerCount
    alivePlayers: list[p] = p.alivePlayerList
    alivePlayerNames: list[str] = p.alivePlayerNames
    os.system("cls")
    print(f"Day {dayCount}")
    if dayCount == 1:
        print(f"Players: {', '.join(alivePlayerNames)}.")
        time.sleep(2)
        return False
    elif dayCount > 1:
        print(f"Players still alive:\n{', '.join(alivePlayerNames)}.")
        wonStatus = checkWon()
        if wonStatus == "Mafia Won.":
            print("Mafia have won the game.")
            return True
        elif wonStatus == "Town Won.":
            print("Town has won the game.")
            return True
        else:
            modPasswordVerification: bool = True
            while modPasswordVerification:
                password: str = input("Enter moderator password:\n")
                if password == "@M3Nexttimemaa":
                    modPasswordVerification = False
                    break
            questions = [ 
            inquirer.List("Vote", 
                message="Start a vote>", 
                choices=["Yes", "No"])]
            answers = inquirer.prompt(questions)
            if answers["Vote"] == "Yes":
                    votedPlayer: p = voteUp(alivePlayerNames=alivePlayerNames, alivePlayers=alivePlayers)
                    voting(votedPlayer = votedPlayer)
                    return False
            elif answers["Vote"] == "No":
                print("Day has ended.")
                time.sleep(2)
            gameWon: bool = checkWon()
            if gameWon == "Mafia Won.":
                print("Mafia have won the game.")
                return True
            elif gameWon == "Town Won.":
                print("Town have won the game.")
                return True
            else:
                return False

