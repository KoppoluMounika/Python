
num = int(input("Enter a number: "))

for i in range(1, 11):
    result = 0
    for _ in range(i):
        result += num
    print(f"{num} x {i} = {result}")
