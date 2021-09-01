from art import logo
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
def add(n1, operation):
  n2 = float(input("\nWhat is the next number?\n> "))
  result = n1 + n2
  print(f"\n{n1} {operation} {n2} = {result}")
  return result

def minus(n1, operation):
  n2 = float(input("\nWhat is the next number?\n> "))
  result = n1 - n2
  print(f"\n{n1} {operation} {n2} = {result}")
  return result

def divide(n1, operation):
  n2 = float(input("\nWhat is the next number?\n> "))
  result = n1 / n2
  print(f"\n{n1} {operation} {n2} = {result}")
  return result

def multiple(n1, operation):
  n2 = float(input("\nWhat is the next number?\n> "))
  result = n1 * n2
  print(f"\n{n1} {operation} {n2} = {result}")
  return result
n1 = 0
result = 0
print(logo)
def choose(againBool, n1, result):
  if againBool == False:
    n1 = float(input("What is the first number?\n> "))
  else:
    n1 = result
  operation = input("\n+\n-\n/\n*\n\nPick an operation:\n> ")
  if operation == "+":
    result = add(n1, operation)
  elif operation == "*":
    result = multiple(n1, operation)
  elif operation == "/":
    result = divide(n1, operation)
  elif operation == "-":
    result = minus(n1, operation)
  else:
    print("\nIncorrect operation :(")

  again = input(f"\nType 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'e' to exit:\n> ")
  
  if again == "n":
    againBool = False
    clear()
    print(logo)
    choose(againBool, n1, result)
  if again == "y":
    againBool = True
    choose(againBool, n1, result)

againBool = False
choose(againBool, n1, result)
print("\nGoodbye.\n")


