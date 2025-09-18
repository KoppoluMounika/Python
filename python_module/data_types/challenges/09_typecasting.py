#Typecasting means converting a variable from one data type to another.

#Implicit Type Conversion - Python automatically converts types where safe.
a = 0.1 + 0.2
print(a == 0.3)  # False due to floating point precision 
#Internally, 0.1 + 0.2 = 0.30000000000000004 due to floating-point error.

#Explicit Type Conversion - manually convert data types using functions like int(), float(), str()
s = "123abc"
num = int(s)   # ValueError: invalid literal for int()





