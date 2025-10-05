#  Sets

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(type(a))
print(len(a))
print(b)
print(type(b))
print(len(b))

#  Sets Traversal

c = {1, 2, 3, 4, 5}
for i in c:
    print(i)


#  Set methods

d = {1, 2, 3}
d.add(4)
print(d)
d.remove(2)
print(d)
d.discard(5)  # Does not raise an error if the element is not found
print(d)
d.pop()  # Removes and returns an arbitrary element
print(d)
d.clear()  # Removes all elements from the set
print(d)
del d  # Deletes the set entirely
# print(d)  # This will raise an error since d is deleted

# set operations


e = {1, 2, 3}
f = {3, 4, 5}

# union

g = e.union(f)
print(g)  # {1, 2, 3, 4, 5}

# intersection

h = e.intersection(f)
print(h)  # {3}

# difference

i = e.difference(f)
print(i)  # {1, 2}

# symmetric difference

j = e.symmetric_difference(f)
print(j)  # {1, 2, 4, 5}

# compound set operations

f -= e
print(f)  # {4, 5}