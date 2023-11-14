# exception =   events detected during
#      execution that interrupt
#      the flow of a program
# Basically, when we have user input, there
# may be instances where we have an error due
# to the wrong input provided by the user.

# And this will cut off any further code
# from being executed.

# To tackle this, we use the "try" and
# "except" block


# "try" command is used to surround
# any code that may generate an error.

# User input is an ideal place to use them.
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
# If we input zero(0) in the denominator,
# then an error prompt will appear which
# states "ZeroDivisionError".

# We write the error after the "except" command
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
# user may divide a number with a string, or
# vice-versa, which will produce "ValueError"
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
# "Exception" is the general error;
# all the errors that are not specified
# are included in here
except Exception as e:
    print(e)
    print("something went wrong :(")
# If no error occurs, then we print the result
else:
    print(result)
# whether or not we catch an exception,
# the finally block will always execute
# at the end
finally:
    print("This will always execute")
# "as e" after the exceptions are not required,
# but it may be helpful if the user wants to
# know the error provided by the program

