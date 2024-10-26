a = int(input("Enter a number: "))
if(a < 0):
    print(f"{a} is a negative number")
elif(a%2 == 0):
    print(f"{a} is an even number")
else:
    print(f"{a} is an odd number")