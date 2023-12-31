# Dean Kurilich
# CS361 Portfolio Project
# This is a program that plays 1-1 game of BlackJack with a player and the dealer.

import random
import sys
import time

# introduction code to define game play
intro_text = "\nHello, Welcome to the BlackJack Card Game program by Dean Kurilich. \n"
print(intro_text)
input("Press enter to continue: ")
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
        self.value = value

    def print_card(self):
        """This function will print a card."""
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
        """This function print a blank card for the dealers first turn."""
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
        self.suits = ["♥", "♦", "♣", "♠"]
        self.values = [("A", "A"), ("K", 10), ("Q", 10), ("J", 10), ("10", 10), ("9", 9), ("8", 8), ("7", 7),
                       ("6", 6), ("5", 5), ("4", 4), ("3", 3), ("2", 2)]
        self.dealt_cards = []

    def generate_card(self):
        """generate a random card from the deck, if the card already exists, it checks for a new card"""
        random_suit = random.randint(1, 3)
        random_value = random.randint(0, 12)
        new_suit = self.suits[random_suit]
        new_name = new_suit + self.values[random_value][0]
        new_value = self.values[random_value][1]
        new_card = Card(new_suit, new_name, new_value)
        if new_card.name not in self.dealt_cards:
            self.dealt_cards.append(new_name)
        else:
            self.generate_card()
        return new_card


class PlayGame:
    """this class defines the black jack game and reference the card and card deck classes. The game is played
    through this class, where the main objects are the dealer and player and their hands and scores"""

    def __init__(self):
        self.player_score = None
        self.dealer_score = None
        self.player_cards = []
        self.dealer_cards = []
        self.card_deck = CardDeck()

    def start_game(self):
        """This function starts the beginning of the game, displaying 1 dealer card face up and 1 face down
        and also displays the initial 2 player cards face up"""
        # reset all local variables
        self.player_score = None
        self.dealer_score = None
        self.player_cards = []
        self.dealer_cards = []
        self.card_deck = CardDeck()
        # deals 2 cards to dealer and player and displays cards in first round of gameplay
        dealer_1 = self.card_deck.generate_card()
        dealer_2 = self.card_deck.generate_card()
        self.dealer_cards.append(dealer_1)
        self.dealer_cards.append(dealer_2)
        player_1 = self.card_deck.generate_card()
        player_2 = self.card_deck.generate_card()
        self.player_cards.append(player_1)
        self.player_cards.append(player_2)
        self.dealer_score = self.calculate_score_microservice(self.dealer_cards)
        print("Dealer Cards:")
        dealer_1.print_blank_card()
        dealer_2.print_card()
        self.player_score = self.calculate_score_microservice(self.player_cards)
        print("Player Cards: ")
        player_1.print_card()
        player_2.print_card()
        self.evaluate_player_score()
        self.continue_gameplay()

    def calculate_score_microservice(self, cards_list):
        """This function takes a hand and calls the microservice to calculate the score"""
        # prints a hand with spaces between values into hand.txt file
        # microservice returns two scores (if A is 1 or 11 points)
        # score is saved in self.player_score or self.dealer_score variable with 2 values as a list (second score is 0
        # if there's no Ace in the hand
        cards_values = []
        for card in cards_list:
            cards_values.append(card.value)
        cards_values = ','.join(str(card) for card in cards_values)
        with open('hand.txt', 'w', encoding="utf-8") as card_hand_file:
            card_hand_file.write(cards_values)
        card_hand_file.close()
        time.sleep(0.1)
        with open('hand_score.txt', 'r+', encoding="utf-8") as card_score_file:
            card_score = card_score_file.read()
        card_score_file.close()
        while card_score == '':
            with open('hand_score.txt', 'r+', encoding="utf-8") as card_score_file:
                card_score = card_score_file.read()
            card_score_file.close()
        card_score = list(card_score.split(","))
        if len(card_score) == 1:
            card_score.append("0")
        return card_score

    def winner(self):
        """Determines if the player has won their turn via a blackjack and displays congratulatory message.
        Else it prompts the player to quit or play again."""
        if "21" in self.player_score:
            print("Congratulations, you have a 21! A BlackJack!")
            print("Player Wins!")
        print()
        play_again = int(input("Type 1 and press enter to play again or type 2 and enter to exit: "))
        if play_again == 1:
            self.start_game()
            return
        elif play_again == 2:
            print()
            print("Goodbye, thanks for playing!")
            sys.exit()
        else:
            print()
            print("Invalid entry, try again.")
            self.winner()

    def loser(self):
        """If a player has busted or lost their hand, they receive losing message and then are prompted to continue
        to the next hand or quit"""
        print()
        print("Sorry, you lose this hand")
        print()
        play_again = int(input("Type 1 and press enter to play again or type 2 and enter to exit: "))
        if play_again == 1:
            self.start_game()
        elif play_again == 2:
            print()
            print("Goodbye, thanks for playing!")
            sys.exit()
        else:
            print()
            print("Invalid entry, try again.")
            self.loser()

    def continue_gameplay(self):
        """"This function reads player input to hit or stay and generates cards and scores with displays accordingly"""
        print()
        next_move = input("Type 1 and enter to hit or type 2 and enter to stay: ")
        if next_move == "1":
            new_card = self.card_deck.generate_card()
            self.player_cards.append(new_card)
            self.player_score = self.calculate_score_microservice(self.player_cards)
            print("Player Cards: ")
            for card in self.player_cards:
                card.print_card()
            self.evaluate_player_score()
            self.continue_gameplay()
        elif next_move == "2":
            if int(self.player_score[0]) < int(self.player_score[1]) <= 21:
                self.player_score[0] = self.player_score[1]
            self.dealer_continue_gameplay()
            return
        else:
            print()
            print("Invalid entry, try again.")
            self.dealer_continue_gameplay()

    def dealer_continue_gameplay(self):
        """If a player decides to stay, then this function is activated to represent the dealer turn."""
        time.sleep(1)
        print("")
        print("Dealer Turn, finalizing hand")
        print("")
        while int(self.dealer_score[0]) < 17:
            if int(self.dealer_score[1]) == 0:
                new_card = self.card_deck.generate_card()
                self.dealer_cards.append(new_card)
                self.dealer_score = self.calculate_score_microservice(self.dealer_cards)
            elif 17 <= int(self.dealer_score[1]) <= 21:
                self.evaluate_dealer_score()
                break
        if int(self.dealer_score[0]) >= 17:
            self.evaluate_dealer_score()

    def evaluate_dealer_score(self):
        """This function determines if the player has a winning or losing hand and displays their score accordingly"""
        if "21" in self.dealer_score:
            print("Sorry, dealer has a 21! A BlackJack!")
            time.sleep(1)
            print("Here is the dealer's final hand:")
            for card in self.dealer_cards:
                card.print_card()
            self.loser()
        elif int(self.dealer_score[0]) > 21:
            if int(self.dealer_score[1]) == 0 or int(self.dealer_score[1]) > 21:
                print("Dealer score: ", str(self.dealer_score[0]))
                print("Dealer busts!")
                time.sleep(1)
                print("Here is the dealer's final hand:")
                for card in self.dealer_cards:
                    card.print_card()
                print("Congratulations! Player wins!")
                self.winner()
        elif int(self.dealer_score[0]) > int(self.dealer_score[1]):
            print("Dealer score: ", str(self.dealer_score[0]))
            if int(self.player_score[0] > self.dealer_score[0]):
                print("Congratulations! Player wins!")
                time.sleep(1)
                print("Here is the dealer's final hand:")
                for card in self.dealer_cards:
                    card.print_card()
                self.winner()
            else:
                print("Sorry, dealer wins.")
                print("Dealer score: ", str(self.dealer_score[0]))
                time.sleep(1)
                print("Here is the dealer's final hand:")
                for card in self.dealer_cards:
                    card.print_card()
                self.loser()

    def evaluate_player_score(self):
        """This function determines if the player has a winning or losing hand and displays their score accordingly"""
        if "21" in self.player_score:
            self.winner()
        elif int(self.player_score[0]) > 21:
            if int(self.player_score[1]) == 0 or int(self.player_score[1]) > 21:
                print("Player score: ", str(self.player_score[0]))
                print("Player busts, Player score over 21")
                self.loser()
        else:
            score_count = 0
            for score in self.player_score:
                if 0 < int(score) < 22:
                    if score_count > 0:
                        print()
                        print("Or")
                        print()
                    score_count += 1
                    print("Player score: ", str(score))


# initialize game and variables
lets_play = PlayGame()

# begin game play
lets_play.start_game()