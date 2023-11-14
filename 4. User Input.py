name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(f"Hello {name}")
print(f"You are {age} years old.")

# But if we want to increase the (age)
# variable by one(1), then we need to use
# this command for input.
# Otherwise, there would be an error in code.

age = int(input("What is your age?: "))
age = age + 1
print(f"After one year, you will be {age} years old. ")

# --------------X-------------------

# Exercise 1: Mad Libs (Mad Libs game is
# where we have a story, but the user gets
# to submit nouns, verbs and adjectives

adjective1 = input(f"Enter an adjective: ")
noun = input(f"Enter a noun: ")
adjective2 = input(f"Enter a second adjective: ")
verb = input(f"Enter an verb: ")
adjective3 = input(f"Enter a third adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

# --------------X-------------------

# Exercise 2: Area Calculation

length = int(input(f"Enter the length of the rectangle: "))
height = int(input(f"Enter the height of the rectangle: "))

print(f"The area of the rectangle is {length * height}")

# --------------X-------------------

# Exercise 3: Shopping Cart

item = input("What item would you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many of this item would you like to buy?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")

# We can round the number to specific
# number of decimal places using this
# command

print(f"Your total is: ${round(total, 2)}")
# "round" is for rounding the number,
# then we write the variable to be
# rounded in first bracket, then we write
# the number of decimal places to round
# off to.
