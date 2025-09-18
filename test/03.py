n=int(input())
r=[]
for i in range(1,n):
    if n%i==0:
        r.append(i)
if sum(r)==n:
    print("it is a perfect number")
else:
    print("it is not a perfect number")