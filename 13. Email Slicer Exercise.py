
email = input("Enter your email: ")

index = email.index("@")
# Index command prints the index of the
# character given in parentheses
print(index)

username = email[:index]
# prints characters from the start to
# the index
domain = email[index + 1:]
# prints characters from the character
# after the index till the end

print(f"Your username is {username} and domain is {domain}")