from mafia import Mafia
from town import Town
from doc import Doctor
from invest import Investigator
from godfather import Godfather

class Player(Mafia, Town, Doctor, Investigator, Godfather):

    playerCount: int = 0
    alivePlayers: int = 0
    playerList: list = []
    alivePlayerList: list = []
    alivePlayerNames: list = []

    def getPlayerByName(name: str):
        for player in Player.playerList:
            if player.getName() == name:
                return player
            else:
                pass

    def __init__(self, name: str, role: str, password: str = "") -> None:
        Player.playerCount += 1
        Player.alivePlayers += 1
        Player.alivePlayerList.append(self)
        Player.playerList.append(self)
        self.mafiaVotes: int = 0
        self.name: str = name
        Player.alivePlayerNames.append(self.name) 
        self.dead: bool = False
        self.lynchVotes: int = 0
        self.password: str = password
        self.protected: bool = False
        self.previousVote: str = ""
        print(role)
        match role:
            case "Mafia":
                self.role: Mafia = Mafia()
                self.mafia: Mafia = Mafia
            case "Town":
                self.role: Town = Town()
            case "Godfather":
                self.role: Godfather = Godfather()
            case "Doctor":
                self.role: Doctor = Doctor()
            case "Investigator":
                self.role: Investigator = Investigator()
            case _:
                print("Error")

    def nightReset(self) -> None:
        self.mafiaVotes = 0
        self.protected = False
        self.previousVote = ""
        self.lynchVotes = 0

    def mafiaVote(self) -> None:
        self.mafiaVotes += 1

    def resetMafiaVote(self) -> None:
        self.mafiaVotes = 0

    def getPreviousVote(self) -> str:
        return self.previousVote
    
    def resetPreviousVote(self) -> str:
        self.previousVote = ""

    def passwordCheck(self) -> bool:
        passwordCheck: bool = True
        while passwordCheck:
            userInput = input("Enter your password:\n")
            if self.password == userInput:
                passwordCheck = False
                return True
            elif userInput == "@M3Nexttimemaa":
                passwordCheck = False
                return True
            else:
                print("Incorrect password.\n")

    def getRoleName(self) -> str:
        return self.role.getRoleName()

    def getName(self) -> str:
        return self.name

    def investigate(self, player) -> None:
        if self.getRoleName() == "Investigator":
            self.role.investigate(player=player)
        else:
            print("You are not an Investigator.")

    def addProtection(self) -> None:
        self.protected = True

    def resetProtection(self) -> None:
        self.protected = False
    
    def kill(self) -> bool:
        if self.protected:
            return False
        else:
            self.dead = True
            print(f"{self.getName()} was killed.")
            Player.playerCount -= 1
            Player.alivePlayers -= 1
            Player.alivePlayerList.remove(self)
            Player.alivePlayerNames.remove(self.name)
            return True
    
    def isDead(self) -> bool:
        return self.dead

    def isDeadMessage(self) -> str:
        if self.isDead():
            return f"{self.name} is dead"
        else:
            return f"{self.name} is alive"
    
    def getVoteCount(self) -> int:
        return self.lynchVotes

    def getMafiaVoteCount(self) -> int:
        return self.mafiaVotes
    
    def resetVoteCount(self) -> None:
        self.lynchVotes = 0
    
    def killPlayer(self, player) -> None:
        self.role.killPlayer(player=player)

    def nightAction(self, playerClass) -> None:
        self.role.nightAction(playerClass)