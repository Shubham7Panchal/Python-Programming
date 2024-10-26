# ##Star Pattern
'''
for n=3
   *
  ***
 *****
'''

# n =  int(input("Enter n = "))
# for i in range(1,n+1):
#     print(" "*(n-i+1), end="")      # here end="" used for printing the
#                                     #next statement within the sameline
#     print("*"*(2*i-1))
#     i+=1





## square
'''
n=5
*****
*   *
*   *
*   *
*****
'''

n =  int(input("Enter n = "))
for i in range(1,(n+1)):
    if(i == 1 or i == n):
        print("*"*n)
    else:
        print("*", end = "")
        print(" "*(n-2), end = "")
        print("*")
    i+=1