# nested loop = A loop within another loop (outer, inner)
#                   outer loop:
#                       inner loop:

for x in range(1, 10):
    print (x, end="")
    # Usually values of x in
    # range are printed on a new line

    # This 'end=""' command is used to dictate
    # how we can arrange the strings that were
    # instead supposed to be printed in new lines
    # (Default for this command is end="\n")
    # Thus it prints strings in a new line

print("")
print("")
# This empty string is printed because even
# the next set of commands are printed in
# the same line as the previous one

# Nested loops:
for x in range(3):
    for y in range(1,10):
        print(y, end="")
    print()
# We need to make sure that for nested
# loops, each counter variable name
# (x and y) should be different

print("")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
       print(symbol, end="")
    print()