from art import logo
print(logo)
def algoritm(alphabet, direction, text, shift):
      new_text = ""
      if direction == "decode":
        shift *= -1
      for letter in text:
        if letter in alphabet:
          letter_pos = alphabet.index(letter)
          letter_pos += shift
          while letter_pos <= len(alphabet):
            letter_pos += len(alphabet)
          while letter_pos >= len(alphabet):
            letter_pos -= len(alphabet)
          new_text += alphabet[letter_pos]
        else:
          new_text += letter
      print(f"\nHere's the {direction}d text: {new_text}") 
def caesar():
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n> ")
  text = input("Type your message:\n> ").lower()
  shift = int(input("Type the shift number:\n> "))
  algoritm(alphabet, direction, text, shift)
  again = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n> ").lower()
  if again == "yes":
    caesar()      
caesar()