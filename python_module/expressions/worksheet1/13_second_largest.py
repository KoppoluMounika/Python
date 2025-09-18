
a = int(input())
b = int(input())
c = int(input())

max_val = a * (a >= b and a >= c) + b * (b >= a and b >= c) + c * (c >= a and c >= b)
min_val = a * (a <= b and a <= c) + b * (b <= a and b <= c) + c * (c <= a and c <= b)
second_largest = a + b + c - max_val - min_val
print(second_largest)
