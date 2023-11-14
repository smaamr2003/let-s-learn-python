
# If the file is in the same directory
# as the Python file, then we just need
# to type the name of the file
with open("example.py") as file:
    print(file.read())

# Otherwise, we need to provide the detailed
# directory of the file
with open("C:\\Users\\pc\\PycharmProjects\\Let's Learn Python\\File Detection using Python.txt") as text:
    print(text.read())
# They automatically close the file after
# opening them. This can be verified using
# the following command:

print(file.closed)
# this will print True or False

# We may like to surround the "open" command
# with "try and except" block, so that if the
# file is not found, it would not interrupt
# the flow of the program


