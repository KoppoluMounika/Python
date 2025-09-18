def sign(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "Zero"
n=int(input())
print(sign(n))