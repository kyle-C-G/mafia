from role import Role
import inquirer
import time

class Town(Role):
    def __init__(self, name: str) -> None:
        super().__init__(roleName="Town")
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
        self.protection = False
        self.previousVote = ""
        return