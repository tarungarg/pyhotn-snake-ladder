from board import *
from player import *
from dice import *


class Play:

    playerPositions = {}
    playedPositions = []
    gotWinner = bool(False)

    def __init__(self, cols=10, rows=10):
        self.rows = rows
        self.cols = cols
        self.initGame()

    def initGame(self):
        self._setBoard()
        self._setPlayer()
        self._prepareTurnsDict()
        self._playTurns()

    def _setBoard(self):
        self.b = Board(self.rows, self.cols)
        self.b.prepareBoard()

    def _setPlayer(self):
        self.p = Player()

    def _prepareTurnsDict(self):
        for x in self.p.players:
            self.playerPositions[x] = {
                "currentPos": 0
            }

    def _playTurns(self):
        print("\n-----------------")
        print("|  Game Start  |")
        print("-----------------\n")

        while self.gotWinner != bool(True):
            for x in self.p.players:
                print("<==================================================>")
                print(("Player {} turn. Please any key to roll the dice\n").format(x))

                if input():
                    diceNumber = Dice().roll()
                    self.b._printSnakeAndLadders()
                    print("You got the number: {}".format(diceNumber))
                    if self._updatePositions(x, diceNumber):
                        continue
                    else:
                        break

    def _updatePositions(self, player, dice):
        gotWinner = bool(False)
        newPos = self.playerPositions[player]["currentPos"] + dice
        if not self._checkForWinner(player, newPos):
            newPos = self.b.getNewPosInCaseSnakeAndLadder(newPos)
            gotWinner = bool(True)

        self.playerPositions[player].update({"currentPos": newPos})
        print("{} new position is {}".format(player, newPos))

        return gotWinner

    def _checkForWinner(self, player, newPos):
        if (newPos >= self.b.rows * self.b.cols):
            self.gotWinner = bool(True)
            return bool(True)

        return bool(False)


if __name__ == '__main__':
    Play()
