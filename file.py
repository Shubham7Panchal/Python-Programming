# # #FILE READ

# f = open("file.txt") #or  f = open("file.txt", "r") 
# data = f.read()
# print(data)
# f.close()

## second way to FILE READ 
# f = open("file.txt")
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()

# ##the same can be written using with statement like below:
# with open("file.txt") as f:                 #<-----imp
#     print(f.read())
#     # now you dont have to explicitly close the file


## FILE READ AS A LIST

# f = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()


# #FILE WRITE: means to write in the blank file

# str1 = "hey there this is your friend, Aisha\n"
# str2 = "yeah we know you"
# f = open("file.txt", "w")
# f.write(str1)
# f.write(str2)
# f.close()
 

## FILE APPENDING: means to add string in the file

# str = "\nlets end the today's session"
# f = open("file.txt", "a")
# f.write(str)
# f.close()


