from role import Role
import inquirer
import time

class Investigator(Role):
    def __init__(self, name: str) -> None:
        super().__init__(roleName="Investigator")
        self.protection: bool = False
        self.previousVote = ""
        self.name: str = name
        self.dead: bool = False

    def killPlayer(self, player) -> None:
        print("You can't kill.")

    def voteFor(self, player) -> None:
        player.lynchVotes["For"] += 1
        self.previousVote = "For"
        return

    def voteAbstain(self, player) -> None:
        player.lynchVotes["Abstain"] += 1
        self.previousVote = "Abstain"
        return

    def voteAgainst(self, player) -> None:
        player.lynchVotes["Against"] += 1
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
        self.protection = False
        self.previousVote = ""
        return