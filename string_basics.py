name = "shubham"
#index number started from 0....from left side
#index number started from -1....from right side
print(name[0:2])    #it is same as print(name[ :2]) or 1st blank space occupied by 0
#OR
print(name[-7:-5])
print(name[2:6])    #it is same as print(name[2:]) or 2nd blank space occupied by string length

print(name[1:7:2])  #it works like below:
"""print(name[1:7]) gives "hubha"
then (name[0:2]) gives "hba" """
#Similarly:-
even_no = "123456789"
print(even_no[1:8:3])
"""print(name[1:8]) gives "2345678"
then (name[0:3]) gives "258" """