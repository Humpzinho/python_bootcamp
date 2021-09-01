#Get a list of names
with open("Day 24 - Mail Merge\\Input\\Names\\invited_names.txt", mode="r") as file:
    names = file.readlines()
    
#Get the letter template
with open("Day 24 - Mail Merge\\Input\\Letters\\starting_letter.txt", mode="r") as file:
    letter = file.readlines()
    letter = "".join(letter)

#Replace [name] for the name at the list of names
for name in names:
    name = name.strip("\n")
    
    with open(
            f"Day 24 - Mail Merge\\Output\\ReadyToSend\\letter_for_{name}.txt", mode="w") as file:
        file.write(letter.replace("[name]", name))