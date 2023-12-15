# This program takes a number grade,
# it determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')
print(" ")

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = len(grades)
avg = sum / 6

x = range(0, 101)
# determine letter grade for average
def letter_grades(avg):
# return letter "A"
  if avg >= 90 and avg <= 100:
    return "A."
  # return letter "B"
  elif avg >= 80 and avg < 90:
    return "B."
  # return letter "C"
  elif avg >= 70 and avg < 80:
    return "C."
  # return letter "D"
  elif avg >= 60 and avg < 70:
    return "D."
  # else return letter "F"
  else:
    return "F."

# - Output
print("\n_________________RESULTS:_________________")
print("Lowest Score: ", low)
print("Highest Score:", high)
print("Grade Average: ", avg)
print("Your grade is a", letter_grades(avg))
print("___________________________________________")
print(" ")