from Dealer import *
from Player import *
from time import sleep

class Game:
    def __init__(self, p_cash):
        self.deck = Deck()
        self.player = Player(p_cash, self.deck)
        self.dealer = Dealer(self.deck)

    def runLoop(self):
        continueGame = True

        while continueGame:
            #clear hands and scores:
            self.player.reset()
            self.dealer.reset()

            # get bet from player:
            bet = self.player.get_bet()

            # Dealer deals two cards to themselves and the player:
            self.deck.shuffle()

            for i in range(2):
                self.dealer.hit()
                self.player.hit()

            # Print hands:
            self.print_currState()

            while not self.player.is_busted and not self.player.is_stand:
                move = self.next_move()
                if move == 'H':
                    self.player.hit()
                    self.print_currState()
                if move == 'S':
                    self.player.stand()

            if self.player.is_busted:
                print("You busted! You lost ${}".format(bet))

            if self.player.is_stand:
                print("You stand")

                # Establish the winning hand for the player
                # (i.e if A is used as 11 or 1)
                if self.player.other_score > 21:
                    player_score = self.player.score
                else:
                    player_score = self.player.other_score

                # Now the dealer plays:
                dealer_score = self.dealer.play()
                self.print_currState()

                if self.dealer.is_busted or (dealer_score < player_score):
                    print("You won!")
                    self.player.cash += (1.5*bet)
                elif dealer_score == player_score:
                    print("It's a tie!")
                    self.player.cash += bet
                else:
                    print("You lost.")
                    self.player.cash -= bet
                print("Your score was {}, and the dealers score was {}".format(player_score, dealer_score))

            if self.player.cash <= 0:
                print("Game over. You've run out of money!")

            print("You now have ${} in cash".format(self.player.cash))

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

    def next_move(self):
        valid_moves = ['H', 'S']
        move = input("What is your next move? (Hit: [H], Stand: [S]\n")

        while move not in valid_moves:
            print("That is an invalid move. Try again:")
            self.next_move()
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