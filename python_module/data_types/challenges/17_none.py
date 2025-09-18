#NONE is a special built-in constant in python that represents the null value
#example for none data type
def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()        
greet("Mounika") 