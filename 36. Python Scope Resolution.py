# variable scope = where a variable is
#                   visible and accessible
# (Basically, it is the order in which the
# value to a variable is specified)

# scope resolution = (LEGB)
#                   1st: Local
#                   2nd: Enclosed
#                   3rd: Global
#                   4th: Built-in


# ---- LOCAL ----

#def func1():
#    a = 1 #local
#    print(b)

#def func2():
#    b = 2 #local
#    print(a)

# The variable inside a function cannot see
# the variable inside the other function.
# Variable is LOCAL to each function

def func1():
    x = 1 #local
    print(x)

def func2():
    x = 2 #local
    print(x)

func1()
func2()
# It prints two different values of x,
# as both values cannot see inside each other

# ---- ENCLOSED ----

def func1():
    x = 1 #enclosed

    def func2():
        #x = 2
        print(x)
    func2()

func1()
# If func2 had x = 2, it would indeed
# return 2, as it is a LOCAL variable
# But since it could not find any variable
# within func2, it then looks at the outer
# variable, where it finds x = 1. Thus it
# returns x = 1.
# Variable is ENCLOSED within the functions
# that are called inside the main function.

# ---- GLOBAL ----

def func1():
    #x = 1
    print(x)

def func2():
    #x = 2
    print(x)

x = 3 #global

func1()
func2()
# Since it does not find any LOCAL variable
# within the function, it searches for the
# GLOBAL variable that is outside of any
# function

# ---- BUILT-IN ----

from math import e

# e = 2.71
def func1():
    print(e)

func1()
# If we had described e = 2.71 as a GLOBAL
# variable, it would have indeed returned
# 2.71
# But since it is not described, it returns
# what is the default value from the module
# In other words, the variable is BUILT-IN