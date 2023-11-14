# indexing = accessing elements of a sequence
#            using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
# prints element at index 0
print(credit_number[0:4])
# prints elements from indexes 0 to 4
print(credit_number[:4])
# prints elements from indexes 0 to 4
# (:4 reads code as starting index to 4)
print(credit_number[4:8])
# prints elements from indexes 4 to 8
print(credit_number[4:])
# prints elements from indexes 4 till the end
print(credit_number[-1])
# prints element of the last index
print(credit_number[-4:])
# prints elements from the fourth to
# last index till the end
# (i.e. from index 15 till the end)
print(credit_number[::2])
# prints elements from beginning to end
# with steps of 2 (i.e. 1st, 3rd, 5th etc.)
print(credit_number[::3])
# prints elements from beginning to end
# with steps of 3 (i.e. 1st, 4th, 7th etc.)

#-------------------X-----------------------

# EXERCISE 1: Print the last four digits

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# EXERCISE 2: Print the credit number
#             backwards

credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1]
print(credit_number)