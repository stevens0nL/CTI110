# CTI - 110, P4T3 - Three Loops
# Laila Stevenson, 10/10/23

# To-Do:
# - For loop
# - WHile loop
# - While with sentinel
# - For each of these, do the following:
# + Ask the user how many cars they saw
# + Find the total and the average

day = 1
MAX_DAYS = 5
cars_today = 0
cars_total = 0
# 1 - For loop
print("Enter how many cars you saw each day")
for day in range(1, MAX_DAYS + 1):
  print("Day #", day, end=": ")
  cars_today = int(input())
  cars_total = cars_total + cars_today
print("Total cars: ", cars_total)
avg = cars_total / MAX_DAYS
print("Average per day: ", avg)
# 2 - While loop
day = 0
MAX_DAYS = 5
cars_today = 0
cars_total = 0
print("\n\n Enter how many cars you saw each day")
while day < MAX_DAYS:
  print("Day #", day, end=": ")
  cars_today = int(input())
  cars_total = cars_total + cars_today
  day = day + 1
print("Total # of cars seen: ", cars_total)
print("Done.")

# 3 - "Sentinel"
cars_total = 0
print("\n\n Enter -1 to finish.")
DONE_VALUE = -1
keep_going = True
while keep_going:
  print("Cars seen today: ", end="")
  cars_today = int(input())
  if cars_today == DONE_VALUE:
    # exit
    keep_going = False
  else:
    # add the value to total
    cars_total = cars_total + cars_today
print("Total cars = ", cars_total)
