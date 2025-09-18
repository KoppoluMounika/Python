d = {'c': [3, 1], 'a': [2, 4], 'b': [5, 1]}
for key in d:
    d[key].sort()
result = sorted(d.items())
print(result)
