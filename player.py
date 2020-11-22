
class Player:
    '''
    The Player object stores the player information
    '''

    players = []

    def __init__(self):
        while True:
            print("Enter number of player wants to play")
            try:
                num = int(input("Please enter a number: "))
                break
            except:
                print("Oops!  Please enter valid number.  Try again...")
        self._askForName(num)

    def _askForName(self, num):
        # It asks for Players information.

        # Parameters:
        #    num (num):The number of player wants to play.

        for x in range(num):
            print("<===================================>")
            print("Enter name for player {}".format(x+1))
            name = input()
            self.players.append(name)

    def showPlayers(self):
        return self.players
