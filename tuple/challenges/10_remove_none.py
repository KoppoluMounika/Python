t = [(None, None), (1, 2), (None, 3), (4, 5), (None, None)]
r = [i for i in t if not (i[0] is None and i[1] is None)]
print(r)