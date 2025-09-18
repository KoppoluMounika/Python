class MyInt(int):
    pass

x = MyInt(10)
print(type(x) == int)# It does not work with subclasses of int      
print(isinstance(x, int)) #This checks if the object is an instance of int or a subclass of int