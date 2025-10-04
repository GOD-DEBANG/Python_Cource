# Lists,

a = [1,2,3,4,5,6,7,8,9,10,True, False, "Hello", "World"]

print(a)
print(a[1:12])

# list indexing

for i in range (len(a)):
    print(a[i])



    # list methods 

a.append("New Item")
print(a)
a.remove("World")
print(a)
a.pop()
print(a)
a.insert(0, "First Item")
print(a)
a.copy()
print(a)
a.count(1)
print(a)

a[0] = "Changed Item"
print(a)

#  Tuple

a = (1, 2, 3, 4, 5)
print(type(a))

# traversing a tuple

for i in range(len(a)):
    print(a[i])

    # Tuple methods
print(a.count(1))
print(a.index(2))

# tuple unpacking

c,d,e,f = (1, 2, 3, 4)
print(e)