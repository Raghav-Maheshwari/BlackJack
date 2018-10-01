from Dealer import *
from Player import *
from time import sleep

class Game:
    def __init__(self, p_cash):
        self.player = Player(p_cash)
        self.dealer = Dealer()
        self.deck = Deck()

    def runLoop(self):
        continueGame = True

        while continueGame:

            # get bet from player:
            while True:
                try:
                    bet = int(input("What is your initial bet? It has to be a minimum of $5\n"))
                    if bet >= 5:
                        if (self.player.cash - bet) < 0:
                            print("Error: You don't have enough cash (You have ${} left)".format(self.player.cash))
                        else:
                            self.player.cash -= bet
                            break
                    else:
                        print("Error: Please enter a positive integer greater than 50")
                except ValueError:
                    print("Error: Please enter a valid amount")
            print("You initially have bet {} amount of dollars. You have ${} left.".format(bet, self.player.cash))

            # Dealer deals two cards to themselves and the player:
            self.deck.shuffle()

            for i in range(2):
                self.hit(self.dealer)
                self.hit(self.player)

            # Print hands:
            self.print_currState()

            while not self.player.is_busted and not self.player.is_stand:
                move = self.next_move()
                if move == 'H':
                    self.hit(self.player)
                    self.print_currState()
                if move == 'S':
                    self.stand(self.player)

            if self.player.is_busted:
                print("You busted!")

            if self.player.is_stand:
                print("You stand")

            while True:
                ask_continue = input("Would you like to play another round, or cash out? "
                                     "(Yes: [Y] | No (cash out): [N])\n")
                if ask_continue == 'N':
                    continueGame = False
                    break
                elif ask_continue == 'Y':
                    continueGame = True
                    break
                else:
                    print("Invalid input")

    def hit(self, player):
        player.hand.append(self.deck.draw_card())

    def stand(self, player):
        player.is_stand = True

    def next_move(self):
        valid_moves = ['H', 'S']
        move = input("What is your next move? (Hit: [H], Stand: [S]\n")

        while move not in valid_moves:
            print("That is an invalid move. Try again:")
            self.ask_action()
        return move

    def print_currState(self):
        print("Dealer is dealing out the cards...\n")
        sleep(1)

        print("Dealer's cards: {}".format(self.dealer.print_hand()))
        print("------------------------------")
        (score, other_score) = self.player.calc_score()
        if score != other_score:
            print("Your cards: {} Current score: {} or {}".format(self.player.print_hand(), score, other_score))
        else:
            print("Your cards: {} Current score: {}".format(self.player.print_hand(), score))