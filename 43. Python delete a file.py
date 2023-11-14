import os
import shutil

path = "C:\\Users\\pc\\OneDrive\\Documents\\Let's Learn Python\\38. File Detection using Python\\File Detection using Python.txt"

try:
    os.remove(path)     #delete a file
    #os.rmdir(path)     #delete an empty directory,
                        #won't delete a directory having 
                        #files in it 
    #shutil.rmtree(path)#delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(f"{path} was deleted")
