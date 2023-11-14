# module = a file containing code we want to
#           include in our program
#
#           use "import" to include a module
#           (built-in or our own)
#
#           useful to break up a large program
#           into reusable separate files

#print(help("modules"))
# prints the list of all available
# built-in modules in Python

# (Type in the name of module within the
# "help" function to get the details of that
# module (existing variables and functions)

#--------------------X---------------------

# We can import a module in three different
# ways:
#import math
# in this case, we need to import a specific
# function via the command, math.pi
#import math as m
# in this case, we need to import a specific
# function via the command, m.pi
#from math import pi
# in this case, we have imported a specific
# function from the math module
# we can use it directly like (2 * pi)

#------------------X---------------------

# we can also make our built-in modules
# and import them into this file
# (For this, we need to create
# two separate files)

import example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)