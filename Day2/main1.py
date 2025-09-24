# operators


# Arithmetic operators

a = 100
b = 20

print("a + b =", a + b) # addition
print("a - b =", a - b) # subtraction
print("a * b =", a * b) # multiplication
print("a / b =", a / b) # division
print("a//b =", a // b) # floor division,means it will give integer value
print("a % b =", a % b) # modulus, it will give remainder
print("a ** b =", a ** b) # exponentiation, means a^b


# Assignment operators

x = 5 # assign 5 to x
print("x =", x)
x += 3 # x = x + 3
print("x after x += 3 is", x)

# Compound assignment operators
#  +=, -=, *=, /=, //=, %=, **=
y = 10
print("y =", y)
y  = 40
print("y after y = 40 is", y)

y = y + 40 # y = 40 + 40
print("y after y = y + 40 is", y)

# insted of y = y + 40 we can write y += 40
y += 40
print("y after y += 40 is", y)
# similarly we can use other compound assignment operators
y -= 20
print("y after y -= 20 is", y)
y *= 2
print("y after y *= 2 is", y)
y /= 4
print("y after y /= 4 is", y)
y //= 3
print("y after y //= 3 is", y)
y %= 3

# Comparison operators
# ==, !=, >, <, >=, <=
# they return boolean values True or False
#  coparison can be done between two numbers, two strings, two lists, two tuples, two sets, two dictionaries and different data types
# but comparison between different data types will always return False except == and != operators
# string and integer comparison using == and != will return False because they are different data types
# but string and string comparison using == and != will return True if both strings are same otherwise False
p = 10
q = 20

print("p == q is", p == q) # False
print("p != q is", p != q) # True
print("p > q is", p > q)   # False
print("p < q is", p < q)   # True
print("p >= q is", p >= q) # False
print("p <= q is", p <= q) # True
print("p == 10 is", p == 10) # True
print("q != 20 is", q != 20) # False
print("p > 5 is", p > 5)   # True
print("q < 30 is", q < 30)   # True
print("p >= 10 is", p >= 10) # True
print("q <= 20 is", q <= 20) # True


# Logical operators
# and, or, not

m = 20
n = 30
g = 40
h = 50

print("m > 10 and n < 40 is", m > 10 and n < 40) # True and True = True
print("m > 10 and n > 40 is", m > 10 and n > 40) # True and False = False
print("m < 10 and n < 40 is", m < 10 and n < 40) # False and True = False
print("m < 10 and n > 40 is", m < 10 and n > 40) # False and False = False
print("g > 30 or h < 60 is", g > 30 or h < 60)   # True or True = True
print("g > 30 or h > 60 is", g > 30 or h > 60)   # True or False = True
print("g < 30 or h < 60 is", g < 30 or h < 60)   # False or True = True
print("g < 30 or h > 60 is", g < 30 or h > 60)   # False or False = False
print("not(m > 10) is", not(m > 10)) # not(True) = False
print("not(n < 40) is", not(n < 40)) # not(True) = False
print("not(g < 30) is", not(g < 30)) # not(False) = True
print("not(h > 60) is", not(h > 60)) # not(False) = True
print("not(m > 10 and n < 40) is", not(m > 10 and n < 40)) # not(True and True) = not(True) = False
print("not(g < 30 or h > 60) is", not(g < 30 or h > 60)) # not(False or False) = not(False) = True


# precedence of logical operators: not > and > or
# so in expression not m > 10 and n < 40, first not m > 10 will be evaluated then and n < 40 will be evaluated


print("not m > 10 and n < 40 is", not m > 10 and n < 40) # False and True = False