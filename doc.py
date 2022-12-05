from role import Role
import inquirer
import time

class Doctor(Role):
    def __init__(self) -> None:
        super().__init__(roleName="Doctor")

    def killPlayer(self, player) -> None:
        print("You can't kill.")
        return

    def voteFor(self, player) -> None:
        player.lynchVotes += 1
        self.previousVote = "For"
        return

    def voteAbstain(self) -> None:
        self.previousVote = "Abstain"
        return

    def voteAgainst(self) -> None:
        self.previousVote = "Against"
        return

    def heal(self, player) -> None:
        player.addProtection()
        print(f"{player.getName()} is protected.")
        return

    def nightAction(self, playerClass) -> list[str]:
        questions = [inquirer.List("Heal", 
            message="Choose who to heal", 
            choices=playerClass.alivePlayerNames)]
        answers = inquirer.prompt(questions)
        player = playerClass.getPlayerByName(answers["Heal"])
        player.addProtection()
        print(f"Protecting {player.getName()}")
        time.sleep(5)