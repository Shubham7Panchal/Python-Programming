## factorial
num = int(input("enter the number whose factorial you want: "))
fact = 1
i=1
while(i<(num+1)):
    fact*=i
    i+=1
print(f"Factorial of {num} is {fact}")