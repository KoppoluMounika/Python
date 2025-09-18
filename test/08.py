n1=int(input())
n2=int(input())
for i in range(n1,n1+100):
    if (i%n1==0) and (i%n2==0):
        print(i)
        break