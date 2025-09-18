n=int(input())
s=str(n)
l=len(s)
sum=0
for i in range(0,l):
    num=int(s[i])
    sum=sum+num**(i+1)
if sum==n:
    print("valid")
else:
    print("not valid")

