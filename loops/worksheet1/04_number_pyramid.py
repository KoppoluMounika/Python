# Function to print the pattern
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


n = int(input())
print_pattern(n)
