# file_path = "example.txt"
# file = open(file_path, "r")
#
# content = file.read
# print(content)
#
# file.close()

import os

#Opening and closing files
file = open("example.txt", "r")
file.close()

#using with statement for automatic closing
with open("example.txt", "r") as file:
    content = file.read()

#Reading from files
with open("example.txt" , "r") as file:
    content = file.read() #Read entire content
    line = file.readline() #Read a single line
    lines = file.readline() #Read all lines into a list

#Writing to files
with open("example.txt" , "w") as file:
    file.write("Hello World")

lines = ["Hello World\n" , "Welcome to Python\n" ]
with open("example.txt" , "w") as file:
    file.writelines(lines)

#Moving the cursor
with open("example.txt" , "r") as file:
    file.seek(0)
    data = file.read()
    print(data)

#Checking file existence
if os.path.exists("example.txt"):
    print("File exists!")

#Appending to file
with open("example.txt" , "a") as file:
    file.write("New data appended")

#Reading and writing binary files
data = b"This is some binary data"
with open("example.bin" , "wb") as file:
    file.write(data)

