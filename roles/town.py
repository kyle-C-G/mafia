from role import Role
import inquirer
import time

class Town(Role):
    def __init__(self) -> None:
        super().__init__(roleName="Town")
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
    
    def nightPrompt(self, playerclass) -> None:
        turnEnded: bool = True
        while turnEnded:
            questions = [inquirer.List("EndTurn", 
                message="Press the correct one to end your turn", 
                choices=["Not this one.", "Not this one.", "This one.", "Not this one."])]
            answers = inquirer.prompt(questions)
            if answers["EndTurn"] == "This one.":
                turnEnded = False
            else:
                pass
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