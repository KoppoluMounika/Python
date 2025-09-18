#in boolean 1 for true and o for False
#1Counting with Boolean Expressions
nums = [1, 2, 3, 4, 5]
even_count = sum(num % 2 == 0 for num in nums)
print("Even numbers:", even_count)

#2 Toggling Values
flag = True
flag = not flag
print(flag)