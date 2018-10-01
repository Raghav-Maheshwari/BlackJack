from Game import *
from time import sleep


def main():
    print("Welcome to Blackjack!")
    quit = False
    while not quit:
        start = input("Would you like to play a game? (Yes: [Y] | No: [N])\n")

        if start == 'Y':
            print("Great!")
            sleep(0.8)
            while True:
                try:
                    cash = int(input("How much cash do you have? Need a minimum of $50 to play\n"))
                    if cash >= 50:
                        break
                    else:
                        print("Error: Please enter a positive integer greater than 50")
                except ValueError:
                    print("Error: Please enter a valid amount")
            print("You're joining the table with {} amount of dollars. Good luck!".format(cash))
            game = Game(cash)
            game.runLoop()

            while True:
                ask_continue = input("Would you like to Quit? (Yes: [Y] | No: [N])\n")
                if ask_continue == 'Y':
                    quit = True
                    break
                elif ask_continue == 'N':
                    break
                else:
                    print("Invalid input")
        elif start == 'N':
            print("Maybe next time!")
            break
        else:
            print("Invalid input")


main()
