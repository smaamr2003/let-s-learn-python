
name = input("Enter your name: ")

#result = len(name)
# This result prints the length of the string
# (which also includes the spaces)

#result = name.find(" ")
# This result gives the first occurence of a
# specific character in a string
# (Note: First index is counted as 0, and
# thereafter counted onwards)

#result = name.find("R")
# When typed "Rakib Abdullah", this result
# prints out as 0, indicating first index
# is denoted as 0.

#result = name.rfind("q")
# "rfind" meaning reverse find
# This result gives the last occurrence of
# a specific character in a string
# (Note: if the code cannot find any
# occurence of a character, it will
# print -1).

#name = name.capitalize()
# This command capitalizes the first letter
# of a string

#name = name.upper()
# This command capitalizes ALL the letters
# of the string

#name = name.lower()
# This command makes ALL the letters of
# a string into lowercase

#result = name.isdigit()
# This command gives the Boolean of whether
# a string contains ONLY numbers

#result = name.isalpha()
# This command gives the Boolean of whether
# a string contains ONLY alphabets
# (Note: It will give the result as False
# even if it contains spaces,
# but does not contain any numbers)

#result = name.count("a")
# This command counts how many desired
# characters are there within a string

replacement = name.replace(" ", "")
# This command replaces a specific character
# in a string with another character
print(replacement)

#print(help(str))
# This command prints a list of string
# methods and their uses


# --------------------X-----------------------
#   EXERCISE: USERNAME VALIDATOR

# validate user input exercise:
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter a username: ")

if len(username) > 12:
   print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1:
   print("Your username can't contain spaces")
elif not username.isalpha():
   print("Your username can't contain digits")
else:
   print(f"Welcome {username}!")

