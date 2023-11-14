# typecasting = The process of
#   converting a value of one data
#   type to another
#   (string, integer, float, boolean)

#   There are two types of typecasting:
#   EXPLICIT and IMPLICIT

name = "Rakib Abdullah"
age = 20
gpa = 4.83
student = True

# If we want to print the data type
# of a variable, then we use this
# command

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# EXPLICIT: Manually converting a
# value or variable into different
# data type

# Examples of EXPLICIT typecasting

# If we want to convert a STRING
# variable to FLOAT variable:

age = float(age)
print(age)
# it prints 21.0 instead of 21

# To convert FLOAT into an INTEGER:

gpa = int(gpa)
print(gpa)
# Only portion before decimal is
# printed

# To convert BOOLEAN into STRING:

student = str(student)
print(student)
print(type(student))
# It prints the same thing, but it is
# now considered as a series of letters

# To convert an INTEGER to a BOOLEAN

age = bool(age)
print(age)
# Any number other than ZERO(0) is
# printed True; if ZERO(0), then False

# IMPLICIT: When a value or variable
# is converted into different data type
# automatically

x = 2
y = 2.0

x = x / y
# RHS: DIVIDING x by y

print(x)
# It prints 1.0 (FLOAT) instead of
# 1 (INTEGER), even though we first
# assigned x value to INTEGER
