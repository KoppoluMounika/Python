s=input()
c=0
for i in s:
    if i.isnumeric():
        c=c+1
if len(s)==c:
    print("it have all digits")
else:
    print("it not have all digits")
