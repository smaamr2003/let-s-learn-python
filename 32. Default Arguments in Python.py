# default arguments = A default value for
#                       certain parameters

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

# These default arguments allow the 
# functions to be more flexible, as we do not need
# to pass all the arguments if we have a default 
# argument, and if we want to change them, then we
# can also change them according to positional 
# arguments.

#-----------------------X-------------------------

import time

def count(end, start = 0):
# The reason "start" is written AFTER "end" 
# is because any default argument has to follow
# positional arguments, otherwise there will be
# SyntaxError
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)

# If we want to change the value 
# of default arguments, then it should 
# be done in order (meaning "end" first, then "start")

count(30, 15)