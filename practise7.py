# ##table 
# num = int(input("Enter a number whose table you want: "))

# # #code1: by for loop
# # for i in range(1,11):
# #     print(f"{num} * {i} = ",i*num)
# #     i += 1

# #code2: by while loop
# i=1
# while(i<11):
#     print(f"{num} * {i} = ",i*num)
#     i+=1


##reverse Mulitplication Table

num = int(input("Enter a number whose table you want: "))
for i in range(1,11):
        print(f"{num} * {11-i} = ",(11-i)*num)
        i += 1
