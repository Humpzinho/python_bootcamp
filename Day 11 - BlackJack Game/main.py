from art import logo
import random
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game():
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':\n> "
             ).lower() != "y":
        clear()
        print("Bye.")
        exit()
    clear()
    print(logo)

    def card_choice(user_cards):
        my_cards_local = []
        card1 = random.choice(cards)
        if card1 == 11 and sum(user_cards) >= 11:
            card1 = 1
        my_cards_local.append(card1)
        return my_cards_local

    my_cards = []
    pc_cards = []
    my_cards = card_choice(my_cards)
    my_cards += card_choice(my_cards)
    pc_cards = card_choice(pc_cards)
    pc_cards += card_choice(pc_cards)

    def final_text():
        print(
            f"    Your final hand: {my_cards}, current score: {sum(my_cards)}")
        print(
            f"    Computer's final hand: {pc_cards}, currect score: {sum(pc_cards)}"
        )

    def text():
        print(f"    Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"    Computer's first card: {pc_cards[0]}")

    def blackjack_result():
        if sum(my_cards) == 21 and sum(pc_cards) == 21:
            final_text()
            print("\nDraw with a Blackjack! 🙃")
            game()
        elif sum(my_cards) == 21:
            final_text()
            print("\nWin with a Blackjack 😎")
            game()
        elif sum(pc_cards) == 21:
            final_text()
            print("\nLose, opponent has Blackjack 😱")
            game()

    blackjack_result()

    while sum(pc_cards) < 17:
        pc_cards += card_choice(my_cards)

    def get_anotherfun(my_cards):
        get_another = input(
            "Type 'y' to get another card, or, type 'n' to pass: ").lower()
        if get_another == "y" and sum(my_cards) < 21:
            my_cards += card_choice(my_cards)
            if sum(my_cards) < 21:
                text()
                get_anotherfun(my_cards)
                
    text()
    get_anotherfun(my_cards)
    blackjack_result()
    final_text()

    if sum(my_cards) == sum(
            pc_cards) or sum(my_cards) > 21 and sum(pc_cards) > 21:
        print("\nDraw 🙃")
        game()
    if sum(pc_cards) > 21:
        print("\nOpponent went over. You win 😁")
        game()
    elif sum(pc_cards) > sum(my_cards) or sum(my_cards) > 21:
        print("\nYou lose. 😤")
        game()
    else:
        print("\nYou win. 😃")
        game()


game()