f=int(input())
if(f<1000):
    print("low brand")
elif(f>=1000 and f<=9999):
    print("mid brand")
elif(f>=10000 and f<=99999):
    print("high brand")
else:
    print("out of range")