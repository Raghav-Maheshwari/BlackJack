from Deck import *

# global variable:
card_map = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10,
    "A": 0
}


class Player:
    def __init__(self, cash, deck):
        self.cash = cash
        self.hand = []
        self.deck = deck
        self.is_stand = False
        self.is_busted = False
        self.score = 0
        self.other_score = 0

    def print_hand(self):
        line = ""
        for card in self.hand:
            line += "[{} of {}] ".format(card.face, card.suite)
        return line

    def calc_score(self):
        global card_map
        self.score = 0
        self.other_score = 0
        for card in self.hand:
            if card_map[card.face] == 0:
                self.other_score += 11
                self.score += 1
            else:
                self.score += card_map[card.face]
                self.other_score += card_map[card.face]

        if self.score > 21 and self.other_score > 21:
            self.is_busted = True

        return self.score, self.other_score

    def get_bet(self):
        # get bet from player:
        while True:
            try:
                bet = int(input("What is your initial bet?\n"))
                if bet > 0:
                    if (self.cash - bet) < 0:
                        print("Error: You don't have enough cash (You have ${} left)".format(self.cash))
                    else:
                        self.cash -= bet
                        break
                else:
                    print("Error: Please enter a positive integer")
            except ValueError:
                print("Error: Please enter a valid amount")
        print("You initially have bet {} amount of dollars. You have ${} left.".format(bet, self.cash))
        return bet

    def hit(self):
        self.hand.append(self.deck.draw_card())

    def stand(self):
        self.is_stand = True

    def reset(self):
        self.score, self.other_score = 0, 0
        self.hand = []
        self.is_stand, self.is_busted = False, False
