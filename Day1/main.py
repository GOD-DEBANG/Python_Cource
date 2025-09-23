sher = 20
name = "Debang-Kuswaha"
print(f"Hello, {name}. You are {sher} years old.")
# Variable can be wirte in 3 ways
# 1. snake_case
# 2. camelCase
# 3. PascalCase
debang_kuswaha = "Debang-Kuswaha"
debangKuswaha = "Debang-Kuswaha"
DebangKuswaha = "Debang-Kuswaha"

print(type(sher))
print(type(name))

# Data types in Python
# 1. int
# 2. float
# 3. str
# 4. bool
# 5. complex
a = 10          # int
b = 10.5        # float
c = "Hello"     # str
d = True        # bool
e = 3 + 5j      # complex
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e)) 

#  string
first_name = "Debang"
last_name = "Kuswaha"
number = "103652254157410847120"

full_name = first_name + " " + last_name
print(full_name)
print(number)

a = 65
print(chr(a))  # ASCII value to character
print(ord('A'))  # character to ASCII value
# String indexing

place = "India"
print(place[0])  # I
print(place[1])  # n
print(place[-1]) # a
print(place[4])  # a


# String slicing

dream = "I want to become a Ai Ml Engineer"
print(dream[0:6:1])      # I want
print(dream[10:16:1])    # become

# type conversion
# example of explicit type conversion
sher = "20"
age = int(sher)
print(type(age))
print(age + 5)
print(type(age + 5))
print(float(age))
print(type(float(age)))
print(str(age))
print(type(str(age)))
print(bool(age))
print(type(bool(age)))
print(complex(age))
# example of impplicit type conversion

x = 10
y = 5.5
z = x + y
print(z)
print(type(z))


# output function

x = 10
naam = "Debang"

print("Hello", naam, "You are", x, "years old.")  # sep = " " by default
# formated String
print(f"Hello {naam}. You are {x} years old.")  # f-string
# raw string
print(r"Hello \n World")  # raw string

# input function

age1 =  input("Enter your name: ")

print("Your name is", age1)




