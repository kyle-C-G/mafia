from role import Role
import inquirer
import time

class Investigator(Role):
    def __init__(self) -> None:
        super().__init__(roleName="Investigator")
        self.protection = False
        self.previousVote = ""

    def killPlayer(self, player) -> None:
        print("You can't kill.")

    def voteFor(self, player) -> None:
        player.lynchVotes += 1
        return
        
    def voteAbstain(self) -> None:
        self.previousVote = "Abstain"
        return

    def voteAgainst(self) -> None:
        self.previousVote = "Against"
        return

    def investigate(self, player) -> None:
        match player.getRoleName():
            case "Mafia":
                print(f"{player.getName()} is a member of the Mafia")
            case "Godfather":
                print(f"{player.getName()} is a member of the Town")
            case "Doctor":
                print(f"{player.getName()} is a member of the Town.")
            case "Investigator":
                print(f"{player.getName()} is a member of the Town.")
            case "Town":
                print(f"{player.getName()} is a member of the Town.")
    
    def nightPrompt(self, playerclass) -> None:
        questions = [inquirer.List("Invest", 
            message = "Choose someone to investigate", 
            choices = playerclass.alivePlayerNames)]
        answers = inquirer.prompt(questions)
        player = playerclass.getPlayerByName(answers["Invest"])
        self.investigate(player=player)
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
        self.protected = False
        self.previousVote = ""
        return