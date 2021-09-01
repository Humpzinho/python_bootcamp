import random
from os import system, name
import time
from hangman_art import stages, logo
from hangman_words import word_list
password = "john123"
try_again = "y"

def game():
  chosen_word = random.choice(word_list)
  passwordinput = input("You are the dev? If you are not, just click enter.\nPassword: ")
  if passwordinput == password:
    change = input(f"\nHey dev, the solution is: '{chosen_word}'\nDo you want to change? Y or N\n> ").lower()
    if change == "y":
      chosen_word = input("\n> ").lower()
      print(f"\n'{chosen_word}' is the new word!\n\nStarting the game...")
      time.sleep(1)
      
    else:
      print("\nOkay, Starting the game...")
      time.sleep(1)
      
  blank = []
  attempts_maked = 0
  remaining_attempts = 0
  remaining_attempts_cli = 6
  correct = False
  stageone = stages[6]
  new_blank = []
  guess_base = ''

  def clear():
    if name == "nt":
      system('cls')
    else:
      system('clear')

  
  for blank_space in range(len(chosen_word)):
    blank += ["_"]

  clear()
  time.sleep(1)
  print(logo)
  print(stages[-remaining_attempts - 1])
  print(f"\n{'  '.join(blank)}\n") 

  while "_" in blank and remaining_attempts != 6:
    attempts_maked += 1
    guess = input("\nGuess a letter:\n> ").lower()
    correct = False

    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if guess == letter:
        blank[position] = guess
        correct = True

    clear()
    if guess not in new_blank and correct == True:
        print(f"Correct!\nRemaining attempts: {remaining_attempts_cli}")
    elif correct == True:
        print("You've already guessed that letter!")

    if correct == False and guess not in guess_base:
      remaining_attempts += 1
      stageone = stages[-remaining_attempts - 1]
      remaining_attempts_cli -= 1
      print(f"Please, Try again.\nRemaining attempts: {remaining_attempts_cli}")
      
    if guess in guess_base and correct == False:
      print("You've already guessed that letter!")

    guess_base += " " + guess
    new_blank = '  '.join(blank)

    
    print(stageone)
    print(f"\n{new_blank}\n")
    print(f"\nTried letters: {guess_base.upper()}\n")

  if remaining_attempts != 6:
    print(f"\nYou won, with {attempts_maked} attemps!\n")
  else:
    clear()
    print(f"Remaining attempts: {remaining_attempts_cli}")
    print(stages[-7])
    print(f"\n{new_blank}\n")
    print(f"You lose, the word was '{chosen_word}'.")
  try_again = input("\nTry again? Y or N.\n> ").lower()
  if try_again == "y":
    clear()
    game()
  else:
    print("\nBye.")

if try_again == "y":
  game()
