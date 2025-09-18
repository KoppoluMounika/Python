def calculate(a,b,choise):
    if choise=="s":
        return a+b 
    elif choise=="d":
        return a-b 
a=int(input())
b=int(input())
choise=input()
print(calculate(a,b,choise))

