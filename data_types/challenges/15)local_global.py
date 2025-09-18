#Local Variable means it is defined inside a function, accessible only within that function.
#Global variable means it is defined outside all functions, acessible antwhere unless shadowed.
#UnboundLocalError-occures when if you tri to access a local variable before its assigned, and also global variable with the same name.
#example for UnboundLocalError
x=10
def exe():
    print(x)
    x=5
    print(x)
exe()
#it returns UnboundLocal Error 
#fix it
x=10
def exe():
    global x
    print(x)
    x=5
    print(x)
exe()