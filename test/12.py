l=list(map(int,input().split()))
k=int(input())
r=[]
for i in l:
    if i<=k and i>=k-5:
        r.append(i)
        break
    elif i>=k and i<=k+5:
        r.append(i)
        break
print(r)