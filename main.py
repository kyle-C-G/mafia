from setup import createXPlayers
from day import day
from player import Player as p
from night import night

def main() -> None:
    createXPlayers()
    gameWon: bool = False
    count: int = 1
    while gameWon == False:
        won = day(dayCount = count)
        if won:
            gameWon = True
            break
        elif won == False:
            night(dayCount = count)
            count += 1
main()