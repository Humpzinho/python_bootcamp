import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\n'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n'''

pc_choice = random.randint(0, 2)

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n\n> "))

picschoice = [rock, paper, scissors]

if choice < 0 or choice > 2:

  print("\nInvalid number, restart the game.")

else:

  print(picschoice[choice])
  print("Computer chose:")
  print(picschoice[pc_choice])

  rockpos = ["Draw.", "You lose.", "You win."]
  paperpos = ["You win.", "Draw.", "You lose."]
  scissorspos = ["You lose.", "You win.", "Draw."]

  endgame = [rockpos, paperpos, scissorspos]

  print(endgame[choice][pc_choice])
