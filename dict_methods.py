a = {}  #here we declare Empty Dict
marks = {
    "ram": 78,
    "ram": 67,
    "shubham": 100,
    99: "hitesh",
    "lekh": 56
}
# print(marks.items())

# print(marks.keys())

# print(marks.values()) 

# marks.update({"shubham": 98, "alekh": 99})
# print(marks)

# print(marks.get("shubham2")) # print None
# print(marks["shubham2"]) # returns an error

# print(marks.popitem())      #pop up the last one item
# print(marks)

print(marks.pop("shubham"))     #pop up the selected item
print(marks)
