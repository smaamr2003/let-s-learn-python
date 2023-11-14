
text = "LINE BREAK \n This part of text is added from a Python file. \n Can you imagine this?"

# "with open" has another argument, which is
# by default 'r', meaning read. But here, we
# are changing it to 'w', meaning write
with open("File Detection using Python.txt", 'w') as file:
    file.write(text)
# This command actually overwrites what was
# previously written, and it happens due to
# 'w' argument

# To add to the existing file, we will pass
# 'a' argument, meaning append