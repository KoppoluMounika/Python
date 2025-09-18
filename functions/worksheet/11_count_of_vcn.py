def string_stats(s):
    vowels="aeiouAEIOU"
    consonants="bcdfghjklmnpqrsetvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    l=len(s)
    v=0
    c=0
    d=0
    for i in s:
        if i in vowels:
            v=v+1 
        elif i in consonants:
            c=c+1 
        elif i.isdigit():
            d=d+1 
    print(v,c,d)
s=input()
string_stats(s)