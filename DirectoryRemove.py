import os
# © Akshaya Simha
# This code attempts to be creating a directory.

dir_name = input("Enter the directory name to be removed: ")
dir_name = dir_name.lower()

if dir_name == "con" or dir_name == "lpt" or dir_name == "prn" or dir_name == "aux":
    print("These names are reserved for Windows operating systems.")
    print("You cannot remove %s." % dir_name)
    
elif os.path.exists(dir_name):
    os.rmdir(dir_name)
    print("Success - Directory is removed.")
    
else:
    print("The directory path does not exist. Check the directory name and then try again.")
