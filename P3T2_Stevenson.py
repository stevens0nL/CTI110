# LAILA STEVENSON
# CTI-110
# 10/04/23 (LATE)
# P3T2

# TODO:
# - make a list for 4 school subjects to use in funct: X
# - write a funct that converts numerical grades to letter grades: X
# - check if user grade avg is failing/passing using else/if:
# - add floats when getting grade avg:

# - ask user for data input on 4 suubjects

english = int(input("What is your grade in English? \n"))
math = int(input("What is your grade in Math? \n"))
science = int(input("What is your grade in Science? \n"))
history = int(input("What is your grade in History? \n"))

grades = [english, math, science, history]
grades2 = english + math + science + history

# varioable for failing/passing

# - else/if function to return letter grades


def letter_grades(grades):
  # return letter "A"
  if grades >= 90 and grades <= 100:
    return "A"
  # return letter "B"
  elif grades >= 80 and grades < 90:
    return "B"
  # return letter "C"
  elif grades >= 70 and grades < 80:
    return "C"
  # return letter "D"
  elif grades >= 60 and grades < 70:
    return "D"
  # **else** return letter "F"
  else:
    return "F"


# write a report for the data
avg = grades2 / 4
letter = letter_grades
print(" ")
print("Your grades have been calculated!")
print("_________________GRADES:_________________")
print("- English:", letter(english))
print("- History:", letter(history))
print("- Math:", letter(math))
print("- Science:", letter(science))
print("Your grade average is:", avg, "%")

fp = avg
if fp >= 60:
  print("With your current grades, you are passing.")

else:
  print("With your current grades, you are failing.")
