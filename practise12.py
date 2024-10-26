# ##factorial

# n = int(input("Enter factorial number: "))

# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*fact(n-1)


# print(f"The factorial of {n} is ",fact(n))

##sum of first n natural number
n = int(input("Enter number upto which you want sum: "))

def natno(n):
    if(n==1):
        return 1
    else:
        return n+natno(n-1)

sum = natno(n)
print(sum)


# ## fibonacci series

# n = int(input("Enter number of terms for fibonacci series: "))

# def fibc(n):
#     if(n<3):
#         for i in range(n):
#             print(i)
#     else:
#         print((n-1)+(n-2))
#         # return (n-1)+(n-2)
        
# fib = fibc(n)
# # print(fib)