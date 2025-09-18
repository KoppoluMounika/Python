l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
r=[]
for i in l1:
    if i not in r and i in l2:
        r.append(i)
print(r)