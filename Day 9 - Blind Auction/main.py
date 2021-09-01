from replit import clear
from art import logo
people = {}
print(logo)

def add_people():
  name = input("\nWhat is your name?\n> ")
  bid = int(input("\nWhat is your bid?\n> $"))
  add_another_people = input("\nAre there any other bidders? Type 'yes or 'no'.\n> ").lower()
  if add_another_people == "yes":
    clear()
    add_people()
  people[name] = bid 
add_people()

maxnumber = 0
for pep in people:
  if people[pep] > maxnumber:
    maxnumber = people[pep]
    maxname = pep

clear()
print("\nThe winner is {}, with a bid of ${}.".format(maxname, maxnumber))