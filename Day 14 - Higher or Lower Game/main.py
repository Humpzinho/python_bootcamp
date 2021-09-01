from art import logo, vs
from game_data import data
import random
import os
def clear(): return os.system('cls' if os.name == 'nt' else 'clear')

clear()
print(logo)

def choice():
    list_choice = random.randint(0, 49)
    return data[list_choice]

total_score = 0
dict_choice_b = choice()
while True:
    dict_choice_a = dict_choice_b
    dict_choice_b = choice()
    print(
        f"Compare A: {dict_choice_a['name']}, a {dict_choice_a['description']}, from {dict_choice_a['country']}")
    print(vs)
    print(
        f"Against B: {dict_choice_b['name']}, a {dict_choice_b['description']}, from {dict_choice_b['country']}")
    if dict_choice_a["follower_count"] > dict_choice_b["follower_count"]:
        winner = "a"
    else:
        winner = "b"
    guess = input("Who was more follower? Type 'A' or 'B': ").lower()
    if guess == winner:
        total_score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {total_score}")
    else:
        print(
            f"""\nSorry, that's wrong. Final score: {total_score}.\n{dict_choice_a['name']} has {dict_choice_a['follower_count']} milions followers, and {dict_choice_b['name']} has {dict_choice_b['follower_count']} milions followers.""")
        again = input("\nDo you want to play again? Type 'y' or 'n': ")
        if again == 'n':
            break
        dict_choice_b = choice()
        clear()
        print(logo)
