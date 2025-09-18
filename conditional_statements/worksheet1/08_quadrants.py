
value = int(input())
if value < 0 or value > 255:
    print("Invalid input. Value must be between 0 and 255.")
else:
    if value <= 63:
        print("Quadrant 1 (0–63)")
    elif value <= 127:
        print("Quadrant 2 (64–127)")
    elif value <= 191:
        print("Quadrant 3 (128–191)")
    else:
        print("Quadrant 4 (192–255)")
