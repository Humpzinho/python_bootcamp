import random
from art import logo

number_guessed = 0
HEALTH = 10
chosen_number = random.randint(1, 100)
game_is_over = False
print(logo)
def distance():
    global HEALTH
    if number_guessed < chosen_number:
        print("\nTo low.")
        print("Guess again.")
        HEALTH -= 1
        print(f"\nYou have {HEALTH} attempts remaining to guess the number.")
    elif number_guessed > chosen_number:
        print("\nTo high.")
        print("Guess again.")
        HEALTH -= 1
        print(f"\nYou have {HEALTH} attempts remaining to guess the number.")
    else:
        print(f"\nYou got it! The answer was {chosen_number}.")
        return True
        
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
#print(f"DEV: Correct anwser: {chosen_number}")
difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "hard":
    HEALTH = 5
print(f"You have {HEALTH} attempts remaining to guess the number.")

while not game_is_over and HEALTH != 0:    
    number_guessed = int(input("\nMake a guess: "))
    game_is_over = distance()
    
if HEALTH == 0:
    print("\nYou've run out of guesses, you lose.")
    

