n=int(input())
s=str(n)
l=len(s)
sum=0
while (l!=1):
    for i in s:
        i=int(i)
        sum=sum+i
    s=str(sum)
    l=len(s)
    sum=0
print(s)


