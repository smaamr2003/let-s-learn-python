# copyfile() = copies contents of a file

# copy() = copyfile() + permission mode
#           + destination can be a directory

# copy2() = copy() + copies metadata
#           (file's creation and
#               modification times)

import shutil

shutil.copyfile()

# The parenthesis contains two parameters:
#   source (src) and destination (dst)

# If we give the dst of the file to be
# something that does not exist,
# it will create new file with the name
# given in the dst, while copying
# the contents of the file

# It also takes the same ruling,
# if the copied file is in the same
# directory as the Python file, then only
# need to write the name of the file. Else,
# we need to provide the complete path
# towards the directory

# copy() and copy2() also take the same
# rulings mentioned above
