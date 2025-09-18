n=int(input())
k=int(input())
print(((n << k) | (n >> (8 - k))) & 0xFF)