from Deck import *
from Player import *


class Dealer(Player):
    def __init__(self, deck):
        super().__init__(self, deck)

    def print_hand(self):
        line = "[Hidden Card] "

        for i in range(1, len(self.hand)):
            line += "[{} of {}] ".format(self.hand[i].face, self.hand[i].suite)

        return line

    def play(self):
        score, other_score = self.calc_score()
        if score == 21 or other_score == 21:
            return score
        else:
            while score < 17:
                self.hit()
                score, other_score = self.calc_score()

                if other_score == 21:
                    return other_score

        if score > 21:
            self.is_busted = True
        return score
