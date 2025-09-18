t = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
avg=[]
for i in range(len(t)):
    a=t[0][i]+t[1][i]+t[2][i]+t[3][i]
    a=float(a//len(t))
    avg.append(a)
print(avg)
