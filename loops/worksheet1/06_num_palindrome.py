def ispalindrome(n):
    o=n
    r=0
    while n>0:
        d=n%10
        r=r*10+d
        n=n//10
    if o==r:
        return 1
    else:
        return 0
n=int(input())
if ispalindrome(n):
    print("the number is palindrome")
else:
    print("the number is not palindrome")