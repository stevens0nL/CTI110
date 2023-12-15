# This program calculates expenses
# 11 / 15 / 2023 (LATE)
# CTI-110 P2HW1 - Travel Expense
# Laila Stevenson

# Variables
budget = float(input("Enter budget: $"))
location = input("Enter your destination: ")
print(" ")
fuel = float(input("Cost of gas: $"))
hotel = float(input("Cost of accom./hotel: $"))
food = float(input("Cost of food: $"))
total = fuel + hotel + food
budget_now = budget - total

print(" ")
print("-------------TRAVEL EXPENSES--------------")
print("Location: ", location)
print("Initial Budget: $", budget)
print("Fuel: $", fuel)
print("Accomodation: $", hotel)
print("Food: $", food)
print("----------------------------------------")
print(" ")
print("Remaining Budget: $", budget_now)

if budget >= total:
  print("You should be able to travel on your budget!")
else:
  print("Your budget is too low to travel.")