from role import Role
import inquirer
import time

class Doctor(Role):
    def __init__(self) -> None:
        super().__init__(roleName="Doctor")
        self.selfProtection: bool = False
        self.protection = False
        self.healedPlayer = 0
        self.previousVote = ""

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

    def voteAgainst(self, player) -> None:
        player.lynchVotes -= 1
        self.previousVote = "Against"
        return

    def heal(self, player) -> None:
        player.addProtection()
        self.healedPlayer = player
        print(f"{player.getName()} is protected.")
        return

    def nightPrompt(self, playerclass) -> list[str]:
        questions = [inquirer.List("Heal", 
            message="Choose who to heal", 
            choices=playerclass.alivePlayerNames)]
        answers = inquirer.prompt(questions)
        player = playerclass.getPlayerByName(answers["Heal"])
        if player == self:
            self.selfHeal()
        else:
            self.healedPlayer = player
        print(f"Protecting {player.getName()}")
        time.sleep(2)
        return

    def nightAction(self, playerclass) -> None:
        if self.healedPlayer != 0:
            healedPlayer = self.healedPlayer
            if self.selfProtection:
                healedPlayer.addProtection()
                return
            elif healedPlayer.isMafiaVoted():
                return
            else:
                healedPlayer.addProtection()
                return
        else:
            return

    def selfHeal(self) -> None:
        self.selfProtection = True
        return

    def kill(self) -> bool:
        if self.selfProtection or self.protection:
            return False
        else:
            self.dead = True
            return True
    
    def nightReset(self) -> None:
        self.healedPlayer = 0
        self.selfProtection = False
        self.protected = False
        self.previousVote = ""