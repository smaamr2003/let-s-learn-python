age = 20
# variable = a reusable container for
# storing a value

# A variable behaves as if it were the
# value it contains

# Given below are the different
# ways to print a statement
# with integer data

print("I am " + str(age) + " years old")
print("I am", age, "years old")
print(f"I am {age} years old")

# f-string are more commonly used
# nowadays, but still one should have
# the knowledge of the other ways

# 4 data types given below
#   1. INTEGER: As the name suggests,
#   it can only be a whole number

players = 2
quantity = 5

print(f"You need {players} players to play a match in Score Match")
print(f"There are only {quantity} items in the shop")

#   2. FLOAT: a number consisting
#   of decimal numbers

gpa = 5.00
price = 5.99

print(f"Your GPA is {gpa}")
print(f"The price for these items is {price}")

#   3. STRING: a series of text or
#   alphabetic characters (it may
#   contain numbers, but those are
#   different than INTEGERS AND FLOATS
#   and are considered to be more like
#   characters)

name = "Rakib Abdullah"
email = "smaamr2003@gmail.com"

print(f"My name is {name}")
print(f"My email address is {email}")

#   4. BOOLEAN: either TRUE or FALSE

online = True
running = False

print(f"Is the player online?: {online}")
print(f"Is the game running?: {running}")

#   Booleans is to be discussed later
#   in the lessons, but it is mainly
#   in 'if' statements

#   One thing to note in Booleans is
#   that it should not be kept in
#   inverted commas, otherwise it acts
#   as Strings, and the first letter
#   of True or False should be in
#   Capital letters

# Variables can be assigned in one
# line of code instead of many lines

x, y, z = 1, 2, 3

print(x)
print(y)
print(z)
print(x, y, z)

# If we want to assign multiple
# variables to the same value, this
# is what we need to do.

x = y = z = 0
print(x, y, z)
