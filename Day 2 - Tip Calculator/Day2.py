
#In English(Excuse my english...Im not native.)

print("Welcome do the tip calculator!\n")

bill = float(input("\nWhat was the total bill?\n> "))

tip = float(input("\nWhat percentage tip would you like to give? 10, 12, or 15?\n> %"))

split = float(input("\nHow many people to split the bill?\n> "))

#Calculate porcentage of the bill
tip_value = tip / 100 * bill
new_bill = tip_value + bill

#Divide by the number of people
new_bill /= split

#Print how much each person should to pay and round to 2 decimals places
print("\nEach person should pay: ${:.2f}".format(new_bill))


#########################################################


#In Portuguese


# print("Olá, Bem-vindo(a) a calculadora de gorjeta!\n")

# bill = float(input("Qual é o valor total da conta?\n> "))

# tip = float(input("\nQual é a porcentagem de gorjeta que você deseja dar? Ex: 12, 10, 15\n> %"))

# split = float(input("\nQuantas pessoas vão dividir a conta?\n> "))

# #Calculate porcentage of the bill
# tip_value = tip / 100 * bill
# new_bill = tip_value + bill

# #Divide by the number of people
# new_bill /= split

# #Print how much each person should to pay and round to 2 decimals places
# print("\nCada pessoa deveria pagar: R${:.2f}".format(new_bill))
