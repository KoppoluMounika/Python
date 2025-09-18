#id(obj) returns the identity (memory address) of the object.
#In CPython (the standard implementation of Python), this is typically the actual memory address.
#example for immutable types
a = 10
b = 10

print(id(a), id(b))      # Likely the same
print(a is b)            # True (due to interning)

b += 1                   # Creates a new object
print(id(b))             # Different now

#example for mutable types

x = [1, 2, 3]
y = x
print(id(x), id(y))      # Same ID — both point to same list
y.append(4)
print(x)                 # x also changed!
print(id(x), id(y))      # Still same — modified in place