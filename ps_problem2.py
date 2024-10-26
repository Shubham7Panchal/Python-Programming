a = "This is not your Dad's hotel, just   pay and get lost"
b = a.find("  ")
print("double space is there in the string:", b!=-1)
#find function detect or find whatever is in double quotes.
print(a.replace("  ", " "))
print(a) #Strings are immutable which means that you cannot change them by running function on them.