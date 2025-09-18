
l=list(map(int,input().split()))
k=int(input())
min=100
for i in range(0,len(l)):
    if ((l[i]<k and k-l[i]<min) or l[i]>k and l[i]-k<min):
        min=l[i]
print(min)