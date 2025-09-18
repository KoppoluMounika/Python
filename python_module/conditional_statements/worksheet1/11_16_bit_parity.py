
value = int(input(),16)
ones_count = bin(value).count('1')
if ones_count % 2 == 0:
    print("Parity: Even")
else:
    print("Parity: Odd")
