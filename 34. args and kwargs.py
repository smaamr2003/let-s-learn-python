# *args    = allows you to pass multiple
#               non-key arguments
# **kwargs = allows you to pass multiple
#               keyword-arguments
#           * unpacking operator

#def add(a, b):
#    return a + b

#print(add(1, 2))

#print(add(1, 2, 3))
# Due to specifying the number of arguments,
# we cannot pass more than two arguments, but
# user input may have more than two arguments

# This is where *args come in handy

#def add(*args):
#    total = 0
#   for arg in args:
#        total += arg
#   return total

# *args arranges all the collections
# into a tuple, so the methods of
# tuple can be applied to args

#print(add(1,2,3,4,5,6))

# name can also be changed to
# another variable instead of args
# (just the * operator must be there)

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3,4,5,6))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Spongebob", "Squarepants")
print()
display_name("Rakib", "Abdullah")
print()
display_name("S.M.", "Abdullah", "Al", "Mahmud", "Rakib")
print()

# **kwargs do the same thing,
# but with keyword arguments

#def print_address(**kwargs):
#    for value in kwargs.values():
#        print(value)

#def print_address(**kwargs):
#    for key in kwargs.keys():
#        print(key)

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(Street="72/7/C-1",
              Area="North Jatrabari",
              District="Dhaka",
              Zip_code="1204")

# **kwargs arrange all the collections
# into a dictionary, we can apply the methods
# of dictionary to **kwargs

#-------------------X---------------------

#def shipping_label(*args, **kwargs):
#    for arg in args:
#        print(arg, end=" ")
#    print()
#    for value in kwargs.values():
#        print(value, end=" ")

# If we want to arrange the kwargs in
# such a way that a specific number of
# arguments are printed on one line and
# the rest are printed on the other, then
# we need to modify our commands using
# old school method

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('Street')}, {kwargs.get('Area')}")
    print(f"{kwargs.get('District')}, {kwargs.get('Zip_code')}")

    # If there is no key with its
    # values, it will print "None"

    # It can be modified using
    # "if" statements

# Need to make sure *args arguments
# are passed first before **kwargs
# arguments

shipping_label("Rakib", "Abdullah",
                Street = "72/7/C-1",
                Area = "North Jatrabari",
                District = "Dhaka",
                Zip_code = "1204")
