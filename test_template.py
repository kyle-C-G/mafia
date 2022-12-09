import unittest
from player import Player
from player import createPlayer

class TestRole(unittest.TestCase):

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