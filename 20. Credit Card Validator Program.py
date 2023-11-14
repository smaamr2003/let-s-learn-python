# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from
#   right to left
# 3. Double every second digit from right
#   to left.
#        (If result is a two-digit number,
#        add the two-digit number together
#        to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10,
#   the credit card number is valid

sum_odd_digits = 0
sum_even_digits = 0
total_sum_digits = 0

# Step 1

credit_card = input("Enter your credit card number: ")
credit_card = credit_card.replace("-", "")
credit_card = credit_card.replace(" ", "")
credit_card = credit_card[::-1]
# This index function reverses the
# credit card number
print(credit_card)

# Step 2

for x in credit_card[::2]:
    sum_odd_digits += int(x)

# Step 3

for x in credit_card[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (round(x / 10) + (x % 10))
    # This could be written as:
    #sum_even_digits += (1 + (x % 10))
    # because maximum value of digit is 9,
    # whose double is 18
    else:
        sum_even_digits += x

# Step 4

total_sum_digits = sum_odd_digits + sum_even_digits

# Step 5

if total_sum_digits % 10 == 0:
    print("VALID")
else:
    print("INVALID")

