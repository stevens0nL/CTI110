import random

def welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of questions and need to answer them correctly.")
    print("Let's get started!")
    print(" ")
  
def get_question_and_answer(question_set):
    question = random.choice(list(question_set.keys()))
    answer = question_set[question]
    return question, answer

def ask_question(question):
    print(question)
    user_answer = input("Enter your answer: ")
    return user_answer

def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer.upper()

def show_score(score):
    print(f"Your current score is: {score}")

def goodbye_message(score):
    print("Thank you for playing the Python Functions Quiz Game!")
    print(f"Your final score is: {score}")

def main():
    score = 0
    
    welcome_message()

    question_set = {
        "Which Pokemon evolves into Pikachu?": "Pichu",
        "What is the largest star in our solar system?": "Sun",
        "Which classic car had an engine called 'Flathead'?": "Ford",
        "What is the currency of Japan?": "Yen"
        # Add more questions and answers here
    }

    for question in range(len(question_set)):
        question, answer = get_question_and_answer(question_set)
        user_answer = ask_question(question)
        
        if check_answer(user_answer, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {answer}.")
        
        show_score(score)
    
    goodbye_message(score)

if __name__ == "__main__":
    main()
