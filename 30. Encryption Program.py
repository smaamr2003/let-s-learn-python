import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
# this prints all the letters and symbols
# that is available in the English language
chars = list(chars)
key = chars.copy()
# a copy of "chars" has been saved so that
# they could be shuffled while keeping the
# original list intact

random.shuffle(key)

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
# For each letter that the user inputs, it
# obtains the index of each letter,
# then for that index, it gets the elements
# (alphabets) at the shuffled "key" list
# and adds to the "cipher_text" variable

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

print()

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")