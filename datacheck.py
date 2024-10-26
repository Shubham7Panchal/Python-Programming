
"""
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
"""
"""with open("data.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        print(number)

with open("data.txt", "w") as file:
    numbers = [10, 20, 30]
    for number in numbers:
        file.write(str(number) + "\n")

with open('data.txt', 'w') as file:
    for number in range(10):
        file.write(f"{number}\n")  # Writing numbers as strings
"""



import csv

file_path = "data.txt"


# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 30, 'New York'],
#     ['Bob', 25, 'Los Angeles']
# ]

# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('data.tsv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(data)

