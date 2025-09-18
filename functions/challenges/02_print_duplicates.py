def duplicates(lst):
    result=[]
    out=[]
    
    for i in lst:
        if i not in result:
            result.append(i)
        elif i not in out:
            out.append(i)
            
            
    return out
print(duplicates([1,2,1,3,2,4]))