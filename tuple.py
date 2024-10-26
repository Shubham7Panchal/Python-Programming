tup = (12,582,5623,12,333, 6)

print(tup.count(12))        # Returns the number of times 12 appears in the tuple

print(tup.index(12))        # Returns the index of the first occurrence of 12 in the tuple.

c,d,e,f,g,h = tup           # Tup Unpacking:Allows you to unpack a tuple into individual variables
print(c,d,e,f,g,h)


print(len(tup))             # return length(or number of elements) in the tuple

#below two can be used among same type of datatypes

print(max(tup))             # Returns the maximum and minimum elements of the tuple

print(min(tup))