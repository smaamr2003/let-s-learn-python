import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
#or   for x in range(my_time, 0, -1):

    seconds = x % 60
    minutes = int(x / 60) % 60
# x / 60 because 1 min = 60 sec, and after
# the division, we want the REMAINDER after
# dividing again by 60, so that minute
# counter does not go above 60
    hours = int(x / 3600)
# The reason % 24 is not written for hours
# is that days are not included in print
# statement, and hours may be greater
# than 24 hours in a timer

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    # :02 = 0 is for zero-padding,
    # and 2 implies 2 spaces for
    # each variable

    time.sleep(1)
# With this command, the program will "sleep"
# for given amount of seconds

print("TIME'S UP!!!")
# The program actually waits for 1 second
# before printing the above prompt