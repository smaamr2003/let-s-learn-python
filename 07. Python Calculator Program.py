num_one = float(input("Enter the 1st number: "))
num_two = float(input("Enter the 2nd number: "))
operator = input("Enter an operator (+ - * /): ")

if operator == "+":
    result = num_one + num_two
    print(round(result, 2))
elif operator == "-":
    result = num_one - num_two
    print(round(result, 2))
elif operator == "*":
    result = num_one * num_two
    print(round(result, 2))
elif operator == "/":
    result = num_one / num_two
    print(round(result, 2))
else:
    print("Not a valid operator.")
