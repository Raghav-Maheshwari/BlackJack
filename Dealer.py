from Deck import *


class Dealer:
    def __init__(self):
        self.deck = Deck()

    def deal_card(self):
        return self.deck.draw_card()
