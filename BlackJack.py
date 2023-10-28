# Dean Kurilich
# CS361 Portfolio Project
# This is a program that plays 1-1 game of BlackJack with a player and the dealer.
#




import random

# introduction code to define game play

intro_text = "\nHello, Welcome to the BlackJack Card Game program by Dean Kurilich. \n"
print(intro_text)
input("Press hit enter to continue: ")
rules = "\nThe rules of the game are as follows: \n\n" \
        "The game is a simple player vs computer match up. The goal of the game is to have a final higher score\n" \
        "than the dealer. If you score higher than 21 you will Bust and automatically lose. To start each game, \n" \
        "the player is dealt two cards from a shuffled, standard 52 card deck. The dealer is also dealt two cards,\n" \
        "however only one of those cards will be visible to you as the player. The player will be prompted with the\n" \
        "option to Hit or Stay. Choosing to Hit means you will be dealt another card, with the potential to improve\n" \
        "your score, but also risking a Bust. Choosing to Stay means the player will keep their current score, and\n" \
        "the dealer's turn will start. The dealer plays using a standard set of rules. If the dealer's score is\n" \
        "less than or equal to 16 then it will always Hit. If the dealer has a soft 17, meaning they have an Ace\n" \
        "and a 6 they will also always Hit. Otherwise the dealer will stay. When the dealer's turn ends, the final\n" \
        "scores are displayed and a message appears on who has won. The scoring is based on the value of each card.\n" \
        "All face cards are worth 10 points, 2 through 9 are with their number value, and an Ace can be 1 or 11\n" \
        "points. If a player is dealt an Ace and a 10 point card, they automatically win with a BlackJack.\n"
print(rules)
start_game = "To start playing press enter: "
input(start_game)

class Card:
    """represents an individual card used in the game"""

    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.card_name = suit + name
        self.value = value

    def print_card(self):
        print(" -------------")
        print("| " + self.suit + "           |")
        print("|             |")
        print("|             |")
        if self.name == "10":
            print("|    " + self.name + "       |")
        else:
            print("|     " + self.name + "       |")
        print("|             |")
        print("|             |")
        print("|           " + self.suit + " |")
        print(" -------------")

    def print_blank_card(self):
        print(" -------------")
        print("|             |")
        print("|             |")
        print("|             |")
        print("|             |")
        print("|             |")
        print("|             |")
        print("|             |")
        print(" -------------")


class CardDeck:
    """This class generates cards for gameplay and tracks cards active in the game"""

    def __init__(self):
        self.suits = ["♥","♦","♣","♠"]
        self.values = [("A", 1), ("K", 10), ("Q", 10), ("J", 10), ("10", 10), ("9", 9), ("8", 8), ("7", 7),
                       ("6", 6), ("5", 5), ("4", 4), ("3", 3), ("2", 2)]
        self.dealt_cards = []

    def generate_card(self):
        random_suit = random.randint(1, 3)
        random_value = random.randint(0, 12)
        new_suit = self.suits[random_suit]
        new_name = self.values[random_value][0]
        new_value = self.values[random_value][1]
        new_card = Card(new_suit, new_name, new_value)
        if new_card.name not in self.dealt_cards:
            self.dealt_cards.append(new_card)
        else:
            self.generate_card()
        return new_card


class PlayGame:

    def __init__(self):
        self.player_score = 0
        self.dealer_score = 0
        self.player_cards = []
        self.dealer_cards = []
        self.card_deck = CardDeck()

    def start_game(self):
        dealer_1 = self.card_deck.generate_card()
        dealer_2 = self.card_deck.generate_card()
        self.dealer_cards.append(dealer_1)
        self.dealer_cards.append(dealer_2)
        player_1 = self.card_deck.generate_card()
        player_2 = self.card_deck.generate_card()
        self.player_cards.append(player_1)
        self.player_cards.append(player_2)
        print("Dealer Cards:")
        dealer_1.print_blank_card()
        dealer_2.print_card()
        print("Player Cards: ")
        player_1.print_card()
        player_2.print_card()


lets_play = PlayGame()
lets_play.start_game()
