from role import Role
import inquirer
import time

class Mafia(Role):

    mafiaMembers = []

    def __init__(self, name: str) -> None:
        super().__init__(roleName="Mafia")
        Mafia.mafiaMembers.append(self)
        self.protection: bool = False
        self.previousVote = ""
        self.name: str = name
        self.dead: bool = False

    def killPlayer(self, player) -> None:
        if player.getRoleName() == "Mafia":
            print("You can't kill another mafia")
        else:
            player.kill()

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
    
    def nightPrompt(self, playerclass) -> list[str]:
        playerList: list[str] = []
        alivePlayerList = playerclass.alivePlayerList
        for player in alivePlayerList:
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
        highestVotedPlayer = {"votes": 0, "player": 0}
        alivePlayerList = playerclass.alivePlayerList
        for player in alivePlayerList:
            if player.getMafiaVoteCount() > highestVotedPlayer["votes"]:
                highestVotedPlayer["player"] = player
        votedPlayer = highestVotedPlayer["player"]
        votedPlayer.kill()

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