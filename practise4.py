num = int(input("Enter a number : "))
#NOTE: i think this code is incomplete without loops
if(num>1):
    if(num == 2 or num == 3 or num == 5 or num == 7 or num == 11):
        print("prime number")
    elif(num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0 or num%11 == 0):
        print("composite number")
else: 
    print("Your have entered number less than 2")