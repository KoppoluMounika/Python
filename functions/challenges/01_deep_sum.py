def deep_sum(lst):
    total = 0
    for item in lst:
        if type(item) == int: 
            total += item
        elif type(item) == list:
            total += deep_sum(item)  
    return total
print(deep_sum([1, [2, [3, 4], 5], 6]))  