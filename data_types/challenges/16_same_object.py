#Yes, in Python, two different variables can refer 
# to the same object in memory.
a = [1, 2, 3]
b = a  # b refers to the same list as a

print(a == b)  #  True — same content
print(a is b)  #  True — same object (same memory)