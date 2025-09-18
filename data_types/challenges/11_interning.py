# String interning is an optimization technique used 
# by Python to reuse immutable string objects rather
# than creating new ones every time
a = "hello"
b = "hello"
print(a == b)  #True → same content
print(a is b)  #True → interned, same memory address

import sys

a = sys.intern("hello world")
b = sys.intern("hello world")

print(a is b)  #True — both point to same memory now
