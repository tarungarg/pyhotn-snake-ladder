import random
from dataclasses import dataclass


@dataclass
class Board:
    rows: int
    cols: int
    board = []
    snakes = []
    ladders = []

    def prepareBoard(self):
        self._createBoardArray()
        self._setSnakes()
        self._setLadders()
        self._printSnakeAndLadders()

    def _printSnakeAndLadders(self):
        self._printSnakes()
        self._printLadders()

    def _createBoardArray(self):
        counter = 1
        for row in range(self.rows):
            arr = []
            for col in range(self.cols):
                arr.append(counter)
                counter += 1
            self.board.append(arr)
        return self.board

    def getNewPosInCaseSnakeAndLadder(self, pos):
        for x in self.snakes:
            if x[0] == pos:
                print(
                    "You cut by snake so have shifted from {} to  {}".format(
                        pos, x[1])
                )
                pos = x[1]
                break

        for x in self.ladders:
            if x[0] == pos:
                print("You got ladder from  {} to {}".format(pos, x[1]))
                pos = x[1]
                break
        return pos

    def _setSnakes(self):
        total = self.rows * self.cols
        for x in range(int(self.rows / 2)-1):
            start = random.randrange(int(total / 2), total)
            start = self._getStartOfSnake(start, total)
            end = random.randrange(0, int((total / 2) - 1))
            self.snakes.append([start, end])
        return self.snakes

    def _setLadders(self):
        total = self.rows * self.cols
        for x in range(int(self.rows / 2)):
            start = random.randrange(0, int((total / 2) - 1))
            end = random.randrange(int(total / 2), total)
            end = self._getStartOfLeader(end, total)
            self.ladders.append([start, end])
        return self.ladders

    def _getStartOfLeader(self, pos, total):
        if self._checkIfSnakeOnSamePosition(pos) or self._checkIfDuplicate(pos, self.ladders):
            pos = random.randrange(0, int((total / 2) - 1))
            self._getStartOfLeader(pos, total)
        return pos

    def _getStartOfSnake(self, pos, total):
        if self._checkIfDuplicate(pos, self.snakes):
            pos = random.randrange(int(total / 2), total)
            self._getStartOfSnake(pos, total)
        return pos

    def _checkIfSnakeOnSamePosition(self, pos):
        snakeExist = bool(False)
        for x in self.snakes:
            if x[0] == pos:
                snakeExist = bool(True)
                break
        return snakeExist

    def _checkIfDuplicate(self, pos, arr):
        duplicateExist = bool(False)
        for x in arr:
            if x[0] == pos:
                duplicateExist = bool(True)
                break
        duplicateExist

    def _printSnakes(self):
        snakeStr = ''
        for snake in self.snakes:
            snakeStr += str(snake[0]) + " ==========> " + str(snake[1]) + "\n"

        print("== == == == == == == == == ===  \
              \nSnakes are at numbers\n{}".format(snakeStr) +
              "======================\n")

    def _printLadders(self):
        ladderStr = ''
        for ladder in self.ladders:
            ladderStr += str(ladder[0]) + \
                " ==========> " + str(ladder[1]) + "\n"

        print("== == == == == == == == == ===\
              \nLadders are at numbers\n{}".format(ladderStr) +
              "========================\n")
