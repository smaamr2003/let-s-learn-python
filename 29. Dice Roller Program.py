# Here are the Unicode characters
# I use for drawing the dice:

# ● ┌ ─ ┐ │ └ ┘

import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

list_of_dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for one_dice in range(num_of_dice):
# one_dice is just a variable, but range is upto input num_of_dice
    list_of_dice.append(random.randint(1, 6))
    # a random dice key:value gets appended to the list_of_dice for num_of_dice times
# PRINT VERTICALLY
for one_dice in range(num_of_dice):
    for each_line in dice_art.get(list_of_dice[one_dice]):
        print(each_line)
# for each of the dice in num_of_dice,
# it prints each of the lines of dice
# for the index that was appended
# to list_of_dice

# PRINT HORIZONTALLY
for each_line in range(5):
    for one_dice in list_of_dice:
        print(dice_art.get(one_dice)[each_line], end="")
    print()
# It is printing the first line of all
# the dices that was appended, then
# it eventually prints all the lines

for one_dice in list_of_dice:
    total += one_dice
print(f"total: {total}")