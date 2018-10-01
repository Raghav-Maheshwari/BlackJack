from Deck import *
from Player import *


class Dealer(Player):
    def __init__(self):
        super().__init__(self)

    def print_hand(self):
        line = "[Hidden Card] "

        for i in range(1, len(self.hand)):
            line += "[{} of {}] ".format(self.hand[i].face, self.hand[i].suite)

        return line