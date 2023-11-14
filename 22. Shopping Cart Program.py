foods = []
prices = []
total = 0

# Lists are used because they can be changed
# according to the user input, and they are
# ordered

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    # The reason food.lower is typed is because
    # user may type in uppercase Q
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print()
print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")