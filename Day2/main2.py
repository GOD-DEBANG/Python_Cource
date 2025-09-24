# Conditional Statements

# if statement

x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement

y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# if-elif-else statement

z = 15
if z < 10:
    print("z is less than 10")
elif z < 20:
    print("z is between 10 and 20")
else:
    print("z is 20 or greater")

# Nested if statement

a = 25
if a > 10:
    if a < 30:
        print("a is between 10 and 30")
    else:
        print("a is 30 or greater")
if a % 2 == 0:
    print("a is even")
else:
    print("a is odd")

# Ternary operator

b = 8
result = "b is even" if b % 2 == 0 else "b is odd"
print(result)

