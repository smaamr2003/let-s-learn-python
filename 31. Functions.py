# function = A block of reusable code
#            {place () after the function name
#            to invoke it

def print_your_info(name, age):
    print(f"Your name is {name}")
    print(f"Your age is {age} years old")
    print("You are a sinful slave of Allah")

print_your_info("Rakib Abdullah", 20)

#--------------------X--------------------

# return = statement used to end a function
#           and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

# Basically, it returns back the answer when
# the function is invoked

print(add(1, 2))
print(subtract(1, 2))

#----------------------X-------------------

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("rakib", "abdullah")

print(full_name)
