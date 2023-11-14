import random

#print(help(random))

#low = 1
#high = 100

#number = random.randint(low, high)
# (prints any random value from "low" to "high")

#number = random.random()
# (prints a random floating point number
# between 0 and 1)

#options = ("rock", "paper", "scissors")
#option = random.choice(options)
# Prints a random option from the tuple "options"

#cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#random.shuffle(cards)
# Shuffles the order of the list "cards"

# --------------------X--------------------

#   EXERCISE: Guessing a random number
#             (with hints)

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Guess a number between ({low} - {high}): "))
    guesses += 1
    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} IS THE CORRECT NUMBER!")
        break

print(f"This round took you {guesses} guesses.")
