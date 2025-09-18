t = [(1, 2), (3, 4), (1, 2), (5, 6)]
n=[]
for i in range(len(t)):
    temp=list(t[i])
    t[i]=temp
for i in t:
    if i not in n:
        n.append(i)
for i in range(len(n)):
    temp=tuple(n[i])
    n[i]=temp
print(n)