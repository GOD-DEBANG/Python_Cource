# Dictionary

d = {}
print(type(d))

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(my_dict)
print(my_dict["name"])

#  CRUD Operations

# Create

my_dict["email"] = "sambhuchowdhury512@gmail.com"
print(my_dict)

# Read

print(my_dict["age"])

# Update

my_dict["name"] = "Debang_Kuswaha"
print(my_dict)

# Delete

del my_dict["city"]

print(my_dict)

#  Iterate

for key in my_dict:
    print(key)


#  Dictionary Methods

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(len(my_dict))
print(my_dict.get("name"))
print(my_dict.pop("age"))
print(my_dict)
print(my_dict.clear())
print(my_dict)
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict.copy())
print(my_dict.fromkeys(["a", "b", "c"], 0))
print(my_dict.setdefault("name", "Default Name"))
print(my_dict)
print(my_dict.update({"age": 31}))
print(my_dict)