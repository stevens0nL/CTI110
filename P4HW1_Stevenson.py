# CTI-110
# P4HW1 - Score List
# Laila Stevenson
# Date

# - Variables
scores = []
score_total = 0
max_score = int(input("How many scores do you want to enter?: "))
print(" ")

# - Loop / Input
scoring = 1
for scoring in range(1, max_score + 1):
  print("Enter score #", scoring, end=": ")
  score = int(input())

  # If-Else
  x = range(0, 101) 
  if score not in x:
    print("Invalid input!\n - Note: Scores should be between 0-100.")
    print("Enter score #", scoring + 1, end=" again: ")
    score = int(input())
  else:
    scores.append(score)
    score_total += score

# - Function
avg = score_total / len(scores)

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
print("Lowest Score: ", min(scores))
print("Modified List:", scores)
print("Score Average: ", score_total / len(scores))
print("Grade: ", letter_grades(avg))
print("___________________________________________")
print(" ")
