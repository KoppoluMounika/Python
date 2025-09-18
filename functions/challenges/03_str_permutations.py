def permutations(s):
    if len(s) == 0:
        return ['']
    
    result = set() 

    for i in range(len(s)):
        char = s[i]
        rest = s[:i] + s[i+1:]
        for perm in permutations(rest):
            result.add(char + perm)
    
    return list(result)
print(permutations("abc"))
