# HOUSE RULES
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


import random
import os
from art import logo


# METHODS
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def check_for_ace(card):
    if card == 11:
        return int(input("\nYou drew an Ace. Would you like a 1 or an 11? "))
    else:
        return card


def calculate_score(cards):
    return sum(cards)


def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You both went over. It's a draw."
    elif player_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win!"
    else:
        if player_score > computer_score:
            return "You win!"
        elif player_score < computer_score:
            return "You lose :("
        else:
            return "It's a draw."


def play():
    print(logo)

    game_is_in_progress = True

    while game_is_in_progress:
        if input("Wanna play Blackjack? (y/n) ") == "y":
            os.system("clear")

            player_score = 0
            computer_score = 0
            player_cards = []
            computer_cards = []
            deal_is_in_progress = True

            while deal_is_in_progress:
                player_cards.append(deal_card())
                computer_cards.append(deal_card())

                player_cards[-1] = check_for_ace(player_cards[-1])

                player_score = calculate_score(player_cards)
                computer_score = calculate_score(computer_cards)

                print(f"Your cards: {player_cards}, score: {player_score}")
                print(f"Computers cards: {computer_cards[0]}")

                if player_score > 21 or computer_score > 21:
                    break

                if input("\nDraw another card? (y/n) ") != "y":
                    break

            print(f"\nYour final hand: {player_cards}, final score: {player_score}")
            print(f"Computers final hand: {computer_cards}, final score {computer_score}")
            print(f"\n{compare(player_score, computer_score)}\n")
        else:
            print("Goodbye")
            game_is_in_progress = False


# MAIN
play()
