def sum_list(lst):  
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])  

n=input()
numbers = list(map(int,n.split()))
print(sum_list(numbers)) 

    