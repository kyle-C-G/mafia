from role import Role
import inquirer
import time

class Investigator(Role):
    def __init__(self) -> None:
        super().__init__(roleName="Investigator")

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
    
    def nightPrompt(self, playerClass) -> None:
        questions = [inquirer.List("Invest", 
            message="Choose someone to investigate", 
            choices=playerClass.alivePlayerNames)]
        answers = inquirer.prompt(questions)
        player = playerClass.getPlayerByName(answers["Invest"])
        self.investigate(player=player)
        time.sleep(5)

    def nightAction(self) -> None:
        return