
t = 50
s1 = int(input())
s2 = int(input())
s3 = int(input())
high_count = (s1 > t) + (s2 > t) + (s3 > t)

if high_count >= 2:
    print("Majority High")
else:
    print("Majority Low")
