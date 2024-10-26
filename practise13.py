## greatest number
l = []
n = int(input("enter number of numbers you have to compare: "))
for items in range(n):
    l.append(int(input(f"Enter number {items+1}: ")))

print(l)

def great(l,n):
    t = l[0]
    # print(t)
    for i in range(1,n):
        if(t<l[i]):
            t = l[i]
    return t

greatest = great(l,n)
print(f"the greatest number from above numbers is {greatest}")