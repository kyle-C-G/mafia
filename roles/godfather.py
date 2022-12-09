from role import Role
import inquirer
import time

class Godfather(Role):
    def __init__(self, name: str) -> None:
        super().__init__(roleName="Godfather")
        self.protection: bool = False
        self.previousVote = ""
        self.name: str = name
        self.dead: bool = False
    
    def killPlayer(self, player) -> None:
        if player.getRoleName() == "Mafia":
            print("You can't kill another mafia")
        else:
            player.kill()
            print(f"You killed {player.getName()}") 

    def voteFor(self, player) -> None:
        player.lynchVotes += 1
        return
        
    def voteAbstain(self, player) -> None:
        self.previousVote = "Abstain"
        return

    def voteAgainst(self, player) -> None:
        self.previousVote = "Against"
        return

    def nightPrompt(self, playerclass) -> list[str]:
        playerList: list[str] = []
        for player in playerclass.alivePlayerList:
            if player.getRoleName() == "Mafia":
                pass
            else:
                playerList.append(player.getName())
        if len(playerList) > 0: 
            questions = [inquirer.List("MafiaVote", 
                message="Vote for the Mafia to kill", 
                choices=playerList)]
            answers = inquirer.prompt(questions)
            votedPlayer = playerclass.getPlayerByName(answers["MafiaVote"])
            votedPlayer.mafiaVote()
        else:
            print("Error")
        time.sleep(2)
    
    def nightAction(self, playerclass) -> None:
        return

    def kill(self) -> bool:
        if self.protection:
            return False
        else:
            self.dead = True
            return True

    def nightReset(self) -> None:
        self.protection = False
        self.previousVote = ""
        return