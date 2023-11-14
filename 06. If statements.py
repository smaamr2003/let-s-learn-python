age = int(input("Enter your age: "))

if age >=100:
    print("You are too old to sign up.")
elif age >= 18:
    print ("You are now signed up!")
elif age < 0:
    print("Invalid age")
else:
    print ("You must be 18+ to sign up")
# The reason age>=100 is written beforehand
# is because age>=18 is still technically
# true if we enter the age above 100 (and code
# runs from top to bottom)

# -------------------X--------------------

#   EXERCISE 1: WOULD YOU LIKE FOOD?

response = input("Would you like to have some food? (Y/N): ")

if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you.")
else:
    print("Invalid response. ")

# -------------------X--------------------

#   EXERCISE 2: "You did not type in your name!"

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

# -------------------X--------------------

#   BOOLEAN CONDITIONS:

for_sale = True
# Change it to either True or False

if for_sale:
    print("This product is for sale.")
else:
    print("This product is NOT for sale.")
