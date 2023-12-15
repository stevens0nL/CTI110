import random

# CTI-110
# P5HW1 - Math Quiz
# LAILA STEVENSON
# 11/07/23

def welc_msg():
  keep_going = True
  while keep_going:
    print(" ")
    print("MAIN MENU")
    print("-------------------------")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Exit")
    print(" ")
    choice = input("Enter your choice: ")

    if choice == '1':
      player_score = add_numbers()
      print(f"Your score is: {player_score}")
      
    elif choice == '2':
      player_score = subtract_numbers()
      print(f"Your score is: {player_score}")
      
    elif choice == '3':
      keep_going = False
      print("Goodbye!")
      
    else:
      print("Invalid choice. Please choose 1, 2, or 3.")


def add_numbers():
  score = 0
  guesses = 0
  plus = '+'
  num3 = random.randint(1, 15)
  num4 = random.randint(1, 15)

  addition = f"{num3} {plus} {num4}"
  answer = eval(addition)
  user_answer = float(input(f"Solve this math problem: {addition} = "))
  guesses += 1

  if user_answer == answer:
    score += 1
    print(f"You are correct! You guessed the number in {guesses} guess(es).")

  else:
    guesses += 1
    print("Your answer is too low or too high. Try again.")
    user_answer = float(input(f"Solve this math problem: {addition} = "))
    # Return the score
    return score
  return guesses
print(" ")


def subtract_numbers():
  score = 0
  guesses = 0
  minus = '-'
  num1 = random.randint(1, 15)
  num2 = random.randint(1, 15)

  subtraction = f"{num1} {minus} {num2}"
  answer = eval(subtraction)
  user_answer = float(input(f"Solve this math problem: {subtraction} = "))
  guesses += 1

  if user_answer == answer:
    score += 1
    print(f"You are correct! You guessed the number in {guesses} guess(es).")
    print(f"Your score is {score}.")

  else:
    guesses += 1
    print("Your answer is too low or too high. Try again.")
    user_answer = float(input(f"Solve this math problem: {subtraction} = "))
    # Return the score
    return score
  return guesses
print(" ")
welc_msg()
