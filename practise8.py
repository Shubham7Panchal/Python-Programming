##program to greet all whoelse in list and whose name starts with letter 's'

l = ["harry", "Shuvbham", "divya", "ronaldo", "suraj", 'Harsh']
print(l)

for item in l:
    if((item.lower()).startswith("s")):
        print(f"\ngreetings!! {item}")
else:
    print("done")         #notice that we use 'else' with 'for' loop statement


