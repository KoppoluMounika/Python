t = ([1, 2], [3, 4], [5, 6])
r= tuple(x for i in t for x in i)
print(r)