
a=int(input())
b=int(input())
c=int(input())
largest = a * (a >= b and a >= c) + b * (b > a and b >= c) + c * (c > a and c > b)
print(largest)