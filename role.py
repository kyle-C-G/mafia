from abc import ABC, abstractmethod

class Role(ABC):
    def __init__(self, roleName: str) -> None:
        self.roleName = roleName
    
    def getRoleName(self) -> str:
        return self.roleName

    @abstractmethod
    def killPlayer(self, player) -> None:
        pass

    @abstractmethod
    def voteFor(self, player) -> None:
        pass

    @abstractmethod
    def nightAction(self) -> None:
        pass

    @abstractmethod
    def voteAbstain(self) -> None:
        pass

    @abstractmethod
    def voteAgainst(self) -> None:
        pass

    @abstractmethod
    def killPlayer(self) -> None:
        pass