n=int(input())
msb=1<<8
if(n&msb):
    print("msb unset")
else:
    print("msg is set")