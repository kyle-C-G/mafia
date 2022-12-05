import os
import time
from player import Player as p
import inquirer
import time

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
    if mafia > town:
        return "Mafia Won."
    elif mafia == 0:
        return "Town Won."
    else:
        return "Game is not over."

 
def day(count) -> bool:
    players: list[p] = p.playerList
    playerCont: int = p.playerCount
    alivePlayers: list[p] = p.alivePlayerList
    alivePlayerNames: list[str] = p.alivePlayerNames
    os.system("cls")
    print(f"Day {count}")
    wonStatus = checkWon()
    if wonStatus == "Mafia Won.":
        print("Mafia have won the game.")
        return True
    elif wonStatus == "Town Won.":
        print("Town has won the game.")
        return True
    else:
        if count == 1:
            print(f"Players: {', '.join(alivePlayerNames)}.")
            time.sleep(5)
        elif count > 1:
            print(f"Players still alive:\n{', '.join(alivePlayerNames)}.")
        print(f"Time remaining: 2 mins.")
        questions = [ 
        inquirer.List("Vote", 
            message="Start a vote>", 
            choices=["Yes", "No"])]
        answers = inquirer.prompt(questions)
        if answers["Vote"] == "Yes":
            os.system("cls")
            questions = [inquirer.List("VoteFor", 
                message="Select a person to stand trial", 
                choices=alivePlayerNames)]
            answers = inquirer.prompt(questions)
            votedPlayer: p = p.getPlayerByName(answers["VoteFor"])
            abstains: int = 0
            votesFor: int = 0
            votesAgainst: int = 0
            player: p
            for player in alivePlayers:
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
                        player.voteFor(votedPlayer)
                    elif answers["PlayerVote"] == "Abstain":
                        player.voteAbstain()
                    elif answers["PlayerVote"] == "Against":
                        player.voteAgainst()
            os.system("cls")
            if votedPlayer.getVoteCount() > ((len(alivePlayers) / 2) - 1):
                playerFor = []
                playerAgainst = []
                playerAbstain = []
                for player in alivePlayers:
                    if player.getPreviousVote() == "Abstain":
                        playerAbstain.append(player.getName())
                    elif player.getPreviousVote() == "For":
                        playerFor.append(player.getName())
                    elif player.getPreviousVote() == "Against": 
                        playerAgainst.append(player.getName())
                time.sleep(5)
                print(f"Players who voted for lynching {votedPlayer.getName()}:\n{', '.join(playerFor)}\n")
                print(f"Players who voted against lynching {votedPlayer.getName()}:\n{', '.join(playerAgainst)}\n")
                print(f"Players who abstained from voting:\n{', '.join(playerAbstain)}\n")
                votedPlayer.kill()
                time.sleep(5)
                return False
            else:
                print(f"{votedPlayer.getName()} was not lynched.")
                print("Day has ended.")
                time.sleep(5)
        elif answers["Vote"] == "No":
            print("Day has ended.")
            time.sleep(5)
        gameWon: bool = checkWon()
        if gameWon == "Mafia Won.":
            print("Mafia have won the game.")
            return True
        elif gameWon == "Town Won.":
            print("Town have won the game.")
            return True
        else:
            return False