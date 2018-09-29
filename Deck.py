from random import shuffle

class Deck:
    def __init__(self):
        cards = []
        suites = ["Hearts", "Diamonds", "Spades", "Clubs"]
        faces = [
            "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K", "A"
        ]
        for suite in suites:
            for face in faces:
                cards.append(Card(face, suite))

        self.cards = cards

    def shuffle(self):
        return shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(-1)


class Card:
    def __init__(self, face, suite):
        self.face = face
        self.suite = suite
