num = int(input("Enter an integer: "))
if num == 0:
    print(0)
else:
    if num < 0:
        print("-", end="")
        num = -num

    while num > 0:
        digit = num % 10
        print(digit, end="")
        num = num // 10