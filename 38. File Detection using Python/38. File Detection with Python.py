import os

path = "C:\\Users\\pc\\Desktop\\Do not read.txt"
# Make sure to provide
# "double" BACKSLASHES (\\)
# (not Slashes (/) ) 
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    # "isdir" is referring to the folders,
    # which in other words is a directory
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")