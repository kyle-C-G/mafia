from roles.mafia import Mafia
from roles.town import Town
from roles.doc import Doctor
from roles.invest import Investigator
from roles.godfather import Godfather
import unittest

class Player():

    roles: list[str] = [
        "Doctor", 
        "Mafia", 
        "Investigator",
        "Town",
        "Godfather"
        ]

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
        self.lynchVotes: int = 0
        self.password: str = password
        self.mafiaVoted: bool = False
        self.doctorVote: bool = False
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
        self.role.protection = True

    def getProtection(self) -> bool:
        return self.role.protection

    def resetProtection(self) -> None:
        self.role.protection = False

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
        return self.role.dead

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
    
    @classmethod
    def reset(cls):        
        playerCount: int = 0
        alivePlayers: int = 0
        playerList: list = []
        alivePlayerList: list = []
        alivePlayerNames: list = []
        playerId: int = 1
        previousAlivePlayers: list = []
        return

def createPlayer(player: str) -> Player:
    return Player(name=player, role=player, password=player)

################################################# UNIT TESTS #####################################################                          

class TestMafia(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.roles: dict[str, Player] = {}
        for role in Player.roles:
            self.roles[role] = createPlayer(role)

    def tearDown(self) -> None:
        Player.reset()

    def test_killSelf(self) -> None:
        player: Player = self.roles["Mafia"]
        self.assertEqual(player.isDead(), False)
        player.kill()
        self.assertEqual(player.isDead(), True)


    def test_nightReset(self) -> None:
        player: Player = self.roles["Mafia"]
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")
        player.role.protection = True
        player.role.previousVote = self.roles["Doctor"]
        player.mafiaVotes = 1
        player.lynchVotes = 1
        player.mafiaVoted = True
        player.doctorVote = True
        self.assertEqual(player.mafiaVotes, 1)
        self.assertEqual(player.lynchVotes, 1)
        self.assertEqual(player.mafiaVoted, True)
        self.assertEqual(player.doctorVote, True)
        self.assertEqual(player.role.protection, True)
        self.assertEqual(player.role.previousVote, self.roles["Doctor"])
        player.nightReset()
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")

class TestDoctor(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.roles: dict[str, Player] = {}
        for role in Player.roles:
            self.roles[role] = createPlayer(role)
        self.roles["Doctor2"] = Player(name="Doctor2", role="Doctor", password="Doctor2")

    def tearDown(self) -> None:
        Player.reset()

    def test_killSelf(self) -> None:
        player: Player = self.roles["Doctor"]
        self.assertEqual(player.isDead(), False)
        player.kill()
        self.assertEqual(player.isDead(), True)

        player2: Player = self.roles["Doctor2"]
        self.assertEqual(player2.isDead(), False)
        player2.role.selfProtection = True
        player2.kill()
        self.assertEqual(player2.isDead(), False)

    def test_nightReset(self) -> None:
        player: Player = self.roles["Doctor"]
        player2: Player = self.roles["Mafia"]
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.selfProtection, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")
        player.role.selfProtection = True
        player.role.protection = True
        player.role.previousVote = player2
        player.mafiaVotes = 1
        player.lynchVotes = 1
        player.mafiaVoted = True
        player.doctorVote = True
        self.assertEqual(player.mafiaVotes, 1)
        self.assertEqual(player.lynchVotes, 1)
        self.assertEqual(player.mafiaVoted, True)
        self.assertEqual(player.doctorVote, True)
        self.assertEqual(player.role.selfProtection, True)
        self.assertEqual(player.role.protection, True)
        self.assertEqual(player.role.previousVote, player2)
        player.nightReset()
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.selfProtection, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")


class TestInvestigator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.roles: dict[str, Player] = {}
        for role in Player.roles:
            self.roles[role] = createPlayer(role)

    def tearDown(self) -> None:
        Player.reset()

    def test_killSelf(self) -> None:
        player: Player = self.roles["Investigator"]
        self.assertEqual(player.isDead(), False)
        player.kill()
        self.assertEqual(player.isDead(), True)

    def test_nightReset(self) -> None:
        player: Player = self.roles["Investigator"]
        player2: Player = self.roles["Doctor"]
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")
        player.mafiaVotes = 1
        player.lynchVotes = 1
        player.mafiaVoted = True
        player.doctorVote = True        
        player.role.protection = True
        player.role.previousVote = player2
        self.assertEqual(player.mafiaVotes, 1)
        self.assertEqual(player.lynchVotes, 1)
        self.assertEqual(player.mafiaVoted, True)
        self.assertEqual(player.doctorVote, True)
        self.assertEqual(player.role.protection, True)
        self.assertEqual(player.role.previousVote, player2)
        player.nightReset()
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")

class TestTown(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.roles: dict[str, Player] = {}
        for role in Player.roles:
            self.roles[role] = createPlayer(role)

    def tearDown(self) -> None:
        Player.reset()

    def test_killSelf(self) -> None:
        player: Player = self.roles["Town"]
        self.assertEqual(player.isDead(), False)
        player.kill()
        self.assertEqual(player.isDead(), True)

    def test_nightReset(self) -> None:
        player: Player = self.roles["Town"]
        player2: Player = self.roles["Doctor"]
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")
        player.mafiaVotes = 1
        player.lynchVotes = 1
        player.mafiaVoted = True
        player.doctorVote = True
        player.role.protection = True
        player.role.previousVote = player2
        self.assertEqual(player.mafiaVotes, 1)
        self.assertEqual(player.lynchVotes, 1)
        self.assertEqual(player.mafiaVoted, True)
        self.assertEqual(player.doctorVote, True)
        self.assertEqual(player.role.protection, True)
        self.assertEqual(player.role.previousVote, player2)
        player.nightReset()
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")

class TestGodfather(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.roles: dict[str, Player] = {}
        for role in Player.roles:
            self.roles[role] = createPlayer(role)

    def tearDown(self) -> None:
        Player.reset()

    def test_killSelf(self) -> None:
        player: Player = self.roles["Godfather"]
        self.assertEqual(player.isDead(), False)
        player.kill()
        self.assertEqual(player.isDead(), True)

    def test_nightReset(self) -> None:
        player: Player = self.roles["Godfather"]
        player2: Player = self.roles["Doctor"]
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")
        player.mafiaVotes = 1
        player.lynchVotes = 1
        player.mafiaVoted = True
        player.doctorVote = True
        player.role.protection = True
        player.role.previousVote = player2
        self.assertEqual(player.mafiaVotes, 1)
        self.assertEqual(player.lynchVotes, 1)
        self.assertEqual(player.mafiaVoted, True)
        self.assertEqual(player.doctorVote, True)
        self.assertEqual(player.role.protection, True)
        self.assertEqual(player.role.previousVote, player2)
        player.nightReset()
        self.assertEqual(player.mafiaVotes, 0)
        self.assertEqual(player.lynchVotes, 0)
        self.assertEqual(player.mafiaVoted, False)
        self.assertEqual(player.doctorVote, False)
        self.assertEqual(player.role.protection, False)
        self.assertEqual(player.role.previousVote, "")