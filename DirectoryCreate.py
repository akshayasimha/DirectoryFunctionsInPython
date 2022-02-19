import os
# © Akshaya Simha
# This code attempts to be creating a directory.

dir_name = input("Enter the directory name to be created: ")
dir_name = dir_name.lower()

if dir_name == "con" or dir_name == "lpt" or dir_name == "prn" or dir_name == "aux":
    print("These names are reserved for Windows operating systems.")
    print("You cannot create the directory named %s." % dir_name)

elif os.path.exists(dir_name):
    print("The directory path already exists. Try another name.")

else:
    os.mkdir(dir_name)
    print("Success - Directory is created.")
