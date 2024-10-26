name = input("enter your name: ")
print(f"Good Morning {name}") ## Note the Way of writing
Date = input("Enter Date: ")
letter = '''Dear Name, 
Congrats!!!
You are selected!
Date'''
print(letter.replace("Name", name).replace("Date", Date))   #this is Chaining of replace string function.
