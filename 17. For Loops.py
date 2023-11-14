# for loops = execute a block of code a fixed
#               number of times.
#               We can iterate over a range,
#               string, sequence etc.

for x in range(1, 11):
   print(x)
# it prints numbers from 1 to 10 (not 11)

print("Countdown Time!!!")

for x in reversed(range(1,11)):
   print(x)
# it prints numbers from 10 to 1 backwards

for x in range(1,11,2):
   print(x)
# it prints numbers in range
# with steps of 2 (i.e.: 1, 3, 5, 7, 9)

credit_card = "1234-5678-9012-3456"

for x in credit_card:
   print(x)

for x in range(1,6):
   if x == 3:
      continue
      # "continue" skips over the numbers
      # given in RHS (prints 1 to 5,
      # skipping 3)
   else:
      print(x)

for x in range(1, 5):
   if x == 3:
       break
       # "break" stops the for loop
       # (or while loop) entirely as
       # the condition is fulfilled
   else:
       print(x)