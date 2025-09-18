#Mutable: Can be changed after creation.
#Immutable: Cannot be changed after creation.
s = "hello"
print(id(s))  # Memory ID before change
s += " world"
print(id(s))

lst = [1, 2, 3]
print(id(lst))  # ID before
lst.append(4)
print(id(lst))