"""
CTI 110
P1HW1 - VARIABLES
Stevenson, L

Do some basic output with numbers
1. Ask for an INT
2. Square it and then cube it
3. Ask for another INT
4. Add them and multiply them


"""


# variables, first and second
first = 0
second = 0

print("Enter integer:")
first = int(input())
print(first, "squared is", first * first,".")
print("and", first, "cubed is", first * first * first,".")

# enter another int
print("Enter another integer:")
second = int(input())
print(first, "+", second, "=", first + second)
print(first, "x", second, "=", first * second)

# Part Two: MOVIES
name = "A Clockwork Orange"
year = 1971
gross = 114.0
quote = " 'Is it better for a man to have chosen evil than to have good imposed upon him?' "

# print out info
# print movie quote
print(name, "is a movie that came out in", year,"and is worth a gross sum of $", gross)
print("A quote from", name, "is --", quote)