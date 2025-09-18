#The values of the objects are equal
#Both variables point to the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  #  True: same content
print(a is b)  # False: different memory locations (two separate lists)

x = 10
y = 10

print(x == y)  # True
print(x is y)  # Also True (but because of small integer caching)
#Python caches small integers (-5 to 256), 
# so x and y may point to the same memory location.

