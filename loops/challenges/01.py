n=int(input())
s=str(n)
l=int(s[0])+int(s[1])
r=int(s[2])+int(s[3])
if l==r:
    print("valid")
else:
    print("not valid")