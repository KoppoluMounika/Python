n=int(input())
a=str(n)
s=0
for i in a:
    i=int(i)
    s=s+i**3
if(n==s):
    print("true")
else:
    print("false")