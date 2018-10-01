from Deck import *

# global variable:
card_map = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10,
    "A": 0
}


class Player:
    def __init__(self, cash):
        self.cash = cash
        self.hand = []
        self.deck = Deck()
        self.is_stand = False
        self.is_busted = False

    def print_hand(self):
        line = ""
        for card in self.hand:
            line += "[{} of {}] ".format(card.face, card.suite)
        return line

    def calc_score(self):
        global card_map
        score = 0
        other_score = 0
        for card in self.hand:
            if card_map[card.face] == 0:
                other_score += 11
                score += 1
            else:
                score += card_map[card.face]
                other_score += card_map[card.face]

        if score > 21 and other_score > 21:
            self.is_busted = True
        return score, other_score



