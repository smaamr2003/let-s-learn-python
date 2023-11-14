# format specifiers = {value:flags} format
#                       a value based on what
#                       flags are inserted
# (They are used in context of an f-string)

#.(number)f = round to that many decimal places
#:(number) = allocate that many spaces
#:0(number) = allocate and zero pad that many spaces
#:< = left justify
#:> = right justify
#:^ = center align
#:+ = use a plus sign to indicate positive value
#:= = place sign to leftmost position
#:  = insert a space before positive numbers
#:, = comma separator
#:% = percentage format

price1 = 3.14159
price2 = -987.65
price3 = 12.34
print(f"price1 is: ${price1:.2f}")
# prints to two decimal place

print(f"price2 is: ${price2:.3f}")
# prints to three decimal places
# (0 is concatenated at the end)

print(f"price3 is: ${price3:}")

print(f"price1 is: ${price1:10}")
# variable now allocates 10 spaces

print(f"price2 is: ${price2:010}")
# numbers would become zero-padded
# (numbers would be preceded by zeros)

print(f"price3 is: ${price3:<10} dollars")
# numbers would occupy 10 spaces, but
# justified towards the left

print(f"price1 is: ${price1:>10}")
# numbers would occupy 10 spaces, but
# justified towards the right (and it is
# also the default justification)

print(f"price2 is: ${price2:^10}")
# numbers would occupy 10 spaces, but
# numbers are now centre aligned

print(f"price3 is: ${price3:+}")
# precedes the positive values with a + sign

print(f"price1 is: ${price1: }")
print(f"price2 is: ${price2: }")
print(f"price3 is: ${price3: }")
# numbers precedes by a space if it is
# a positive number

price1 = 30000.14159
price2 = -9870.65
price3 = 1200.34

print(f"price1 is: ${price1:,}")
print(f"price2 is: ${price2:,}")
print(f"price3 is: ${price3:,}")
# comma separator

print(f"price1 is: ${price1:+,.2f}")
print(f"price2 is: ${price2:+,.2f}")
print(f"price3 is: ${price3:+,.2f}")
# Format specifiers combined
# (preceding plus sign, comma separator,
# and two decimal places)