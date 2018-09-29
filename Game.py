from Dealer import *
from Player import *

class Game:
    def __init__(self, p_cash):
        self.player = Player(p_cash)
        self.dealer = Dealer()
        self.continueGame = True



    card_map = {
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10,
        "A": 0
    }
