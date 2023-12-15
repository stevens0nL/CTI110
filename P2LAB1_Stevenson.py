mileage = float(input("Enter the car's mileage (miles/gallon): "))
gas_cost = float(input("Enter the cost of gas (dollars/gallon): "))
cost_20_miles = 20 / mileage * gas_cost
cost_75_miles = 75 / mileage * gas_cost
cost_500_miles = 500 / mileage * gas_cost
print(f'{cost_20_miles:.2f} {cost_75_miles:.2f} {cost_500_miles:.2f}')
