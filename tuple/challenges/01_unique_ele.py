def unique(t):
    t=set(t)
    t=tuple(t)
    return t

t=tuple(map(int,input().split()))
r=unique(t)
print(r)