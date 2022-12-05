from role import Role
import inquirer
import time

class Godfather(Role):
    def __init__(self) -> None:
        super().__init__(roleName="Godfather")
    
    def killPlayer(self, player) -> None:
        if player.getRoleName() == "Mafia":
            print("You can't kill another mafia")
        else:
            player.kill()
            print(f"You killed {player.getName()}") 

    def voteFor(self, player) -> None:
        player.lynchVotes += 1
        return
        
    def voteAbstain(self) -> None:
        self.previousVote = "Abstain"
        return

    def voteAgainst(self) -> None:
        self.previousVote = "Against"
        return

    def nightAction(self, playerClass) -> list[str]:
        playerList: list[str] = []
        for player in playerClass.alivePlayerList:
            if player.getRoleName() == "Mafia":
                pass
            else:
                playerList.append(player.getName())
        if len(playerList) > 0: 
            questions = [inquirer.List("MafiaVote", 
                message="Vote for the Mafia to kill:", 
                choices=playerList)]
            answers = inquirer.prompt(questions)
            votedPlayer = playerClass.getPlayerByName(answers["MafiaVote"])
            votedPlayer.mafiaVote()
        else:
            print("Error")
        time.sleep(5)