# 10/04/2023 (LATE)
# CTI-110 P1HW2 - Travel Expense
# LAILA STEVENSON

# TO-DO:
# - Ask user to enter their budget: X
# - Ask user to enter travel destination: X
# - Ask user for amount they will spend on gas: X
# - Ask user for amount they will spend on accommodation: X
# - Ask user for amount they will spend on food: X
# - Add expenses: 
# - Subtract expenses from budget + Display results: 

budget = int(input("What is your travelling budget? \n : $"))
location = input(("Please enter your destination. \n : "))
gas = int(input("How much will you spend for gas? \n : $"))
acc = int(input("How much will you spend on accomodations? \n : $"))
food = int(input("How much will you spend on food? \n : $"))

print("Your expenses have been claculated! \n")

total = gas + acc + food
budget2 = budget - total

print("Travel to ", location, "will equal about up to: $",total,".")
print("With your budget of $",budget, "you will be left with $",budget2, ".")

if budget2 < budget:
  print("The travel expenses exceed your given budget.")
else:
  print("With your current budget, you can enjoy travelling.")