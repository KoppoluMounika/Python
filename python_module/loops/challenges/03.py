n=int(input())
sum=0
if n<1000:
    s=str(n)
    for i in s:
        num=int(i)
        f=1
        for i in range(1,num+1):
            f=f+i 
        sum=sum+f
if sum==n:
    print("valid")
else:
    print("not valid")
