fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0])
# This prints the entire list of fruits

print(groceries[0][0])
# This prints the 1st element from the
# 1st list (treat them as coordinates (x,y))

# We can also make 2D lists like this:
groceries = [["apple", "orange", "banana", "coconut"],
["celery", "carrots", "potatoes"],
["chicken", "fish", "turkey"]]

for items in groceries:
    for item in items:
        print(item, end=" ")
    print()

# Variants of 2D collections:
#   1. a List of Tuples
#   2. a Tuple of Tuples
#   3. a Tuple of Sets

#----------------------X--------------------

#   EXERCISE: Creating 2D number keypad

# For this, a tuple is used because it is
# ordered and unchangeable, and it is
# faster

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()
