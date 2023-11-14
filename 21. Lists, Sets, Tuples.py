# collection = single "variable" used to
# store multiple values

#   List = [] ordered and changeable.
#   Duplicates OK

#   Set = {} unordered and immutable,
#   but Add/Remove OK. NO duplicates

#   Tuple = () ordered and unchangeable.
#   Duplicates OK. Faster

#   LIST:

fruits = ["apple", "orange", "banana", "coconut"]

#print(fruits)
#print(fruits[0])
# for accessing each of the elements
# in the list

#print(fruits[:3])
# gives the list of only first
# three elements in the "fruits" list

#for fruit in fruits:
#    print(fruit)
# prints each of the elements in a
# different line
# (common naming convention among the
# Python developers is to write the
# singular version of the list as counter)

#print(dir(fruits))
# prints the string methods we can conduct
# with a collection

#print(help(fruits))
# prints the descriptive list of string
# methods

#print(len(fruits))
# prints how many elements there are
# in the list

#print("apple" in fruits)
# prints Boolean of whether a specific
# element is a part of the list

#fruits[0] = "pineapple"

#for fruit in fruits:
#    print(fruit)

#fruits.append("pineapple")
# Adds an element at the end of the list

#fruits.remove("apple")
#fruits.insert(0, "pineapple")
#fruits.sort()
# Sorts the list in alphabetical order

#fruits.reverse()
# Reverses the order of elements in the list

#fruits.clear()
# The list is cleared and all the elements
# are removed

print(fruits.index("apple"))
# prints the index of an element in the list

#print(fruits.count("banana"))
# Counts how many of an element there is.
# (Same element can be present more than
# one times)
#print(fruits)

#   SETS:

#fruits = {"apple", "orange", "banana", "coconut"}
# Sets are unordered, thus every time
# we run the code, we get an output of
# different order

# And if we include any elements twice
# (duplicating), it will give output
# only one time

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)
#fruits.add("pineapple")
#fruits.remove("banana")
#fruits.pop()
# It removes the first element of the set,
# but it is random as they are unordered

#fruits.clear()

# As sets are unordered, we cannot print
# their indexes

#   TUPLES:

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("apple" in fruits)
#print(fruits.index("apple"))
#print(fruits.count("banana"))
#for fruit in fruits:
#    print(fruit)