friends = 2

#   ADDITION:
#friends = friends + 1
#friends += 1
# Both ways can be used to add values

#   SUBTRACTION:
#friends = friends - 2
#friends -= 2
# Both ways can be used to subtract values

#   MULTIPLICATION:
#friends = friends * 3
#friends *= 3
# Both ways can be used to multiply values

#   DIVISION:
#friends = friends / 2
#friends /= 2
# Both ways can be used to divide values

#   EXPONENT:
#friends = friends ** 2
#friends **= 2
# Both ways can be used to raise
# to the power of some other value

#   MODULUS (REMAINDER):
#remainder = friends % 5
# This gives us the remainder of the
# division conducted between two numbers

print(friends)

#----------------------X--------------

#   BUILT-IN MATH FUNCTIONS:

x = 3.14
y = -4
z = 5

#   ROUNDING:
#result = round(x)
# This function rounds off the float
# to an integer

#   ABSOLUTE VALUE (MODULUS):
#result = abs(y)
# This function gives the modulus of
# the number

#   POWER (EXPONENT):
result = pow(4, 3)
# This function represents first value
# raised to the power of second value

#   MAXIMUM VALUE AND MINIMUM VALUE:
#result = max(x, y, z)
# This function gives the maximum value
# among a group of data

#result = min(x, y, z)
# This function gives the minimum value
# among the group of data
print(result)

#----------------------X--------------

#   MATH MODULE:

import math

print(math.pi)
# PI constant

print(math.e)
# Exponential constant

print(math.sqrt(9))
# Square root of a number

print(math.ceil(3.114))
# prints the rounded number to the
# uppermost value (in this case, 4)

print(math.floor(3.9867))
# prints the rounded number to the
# lowermost value (in this case, 3)

#----------------------X--------------

# Exercise 1: Circumference of a circle

import math

#radius = float(input("Enter the radius of a circle: "))

#circumference = 2 * math.pi * radius

#print(f"The circumference is {round(circumference,2)}")

#----------------------X--------------

# Exercise 2: Area of a circle

import math

radius = float(input("What is the radius of the circle?: "))

#area = math.pi * (radius ** 2)
area = math.pi * pow(radius, 2)

print(f"The area of the circle is {round(area, 2)}")

#----------------------X--------------

# Exercise 3: Hypotenuse of a right-angled triangle

import math

a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Length of hypotenuse is {round(c, 2)}")