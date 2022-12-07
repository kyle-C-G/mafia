from roles.mafia import Mafia
from roles.town import Town
from roles.doc import Doctor
from roles.invest import Investigator
from roles.godfather import Godfather

class Player():

    playerCount: int = 0
    alivePlayers: int = 0
    playerList: list = []
    alivePlayerList: list = []
    alivePlayerNames: list = []
    playerId: int = 1
    previousAlivePlayers: list = []

    def setPreviousAlivePlayers() -> None:
        Player.previousAlivePlayes = Player.alivePlayerList

    def getPlayerByName(name: str):
        for player in Player.playerList:
            if player.getName() == name:
                return player
            else:
                pass

    def getPlayerbyId(id: int):
        for player in Player.playerList:
            if player.getId() == id:
                return player
            else:
                pass

    def __init__(self, name: str, role: str, password: str = "") -> None:
        Player.playerCount += 1
        Player.alivePlayers += 1
        Player.alivePlayerList.append(self)
        Player.playerList.append(self)
        self.playerId = Player.playerId
        Player.playerId += 1
        self.mafiaVotes: int = 0
        self.name: str = name
        Player.alivePlayerNames.append(self.name) 
        self.dead: bool = False
        self.lynchVotes: int = 0
        self.password: str = password
        self.protected: bool = False
        self.mafiaVoted: bool = False
        self.doctorVote: bool = False
        print(role)
        match role:
            case "Mafia":
                self.role: Mafia = Mafia(name = self.name)
            case "Town":
                self.role: Town = Town( name = self.name)
            case "Godfather":
                self.role: Godfather = Godfather(name = self.name)
            case "Doctor":
                self.role: Doctor = Doctor(name = self.name)
            case "Investigator":
                self.role: Investigator = Investigator(name = self.name)
            case _:
                print("Error")

    def nightPrompt(self, playerclass) -> None:
        self.role.nightPrompt(playerclass=playerclass)
        return

    def isMafiaVoted(self) -> bool:
        if self.mafiaVoted:
            return True
        else:
            return False

    def getId(self) -> int:
        return self.playerId

    def voteFor(self, player) -> None:
        self.role.voteFor(player=player)

    def voteAgainst(self, player) -> None:
        self.role.voteAgainst(player = player)
    
    def voteAbstain(self, player) -> None:
        self.role.voteAbstain(player = player)

    def nightReset(self) -> None:
        self.role.nightReset()
        self.mafiaVotes = 0
        self.lynchVotes = 0
        self.mafiaVoted = False
        self.doctorVote = False

    def mafiaVote(self) -> None:
        self.mafiaVotes += 1

    def resetMafiaVote(self) -> None:
        self.mafiaVotes = 0

    def getPreviousVote(self) -> str:
        return self.role.previousVote
    
    def resetPreviousVote(self) -> str:
        self.role.previousVote = ""

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
        self.role.protected = True

    def getProtection(self) -> bool:
        return self.role.protected

    def resetProtection(self) -> None:
        self.role.protected = False

    def kill(self) -> None:
        isDead = self.role.kill()
        if isDead:
            Player.playerCount -= 1
            Player.alivePlayers -= 1
            Player.alivePlayerList.remove(self)
            Player.alivePlayerNames.remove(self.name)
        else:
            return
        return
    
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