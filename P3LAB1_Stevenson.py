# CTI-110, M3 Lab1 - Leap Year
# Stevenson, L - 09/21/23

# Calculate if a year is a leap year
# Leap year = divisible by 4 (unless it's a century, it's divisible by 400)

# TODO : Handle the century case
is_leap_year = False

print("Enter a year to check: ")
year = int(input())

# Refer to comments on leap years
# We use %, the modular operator
if year % 4 == 0:
  is_leap_year = True

# Century exception: if it's divisble by 100
if year % 100 == 0:
  # then it isn't a leap year
  is_leap_year = False
  if year % 400 == 0:
    is_leap_year = True

if is_leap_year:
  print(year, "is a leap year!")
else:
  print(year, "isn't a leap year.")
