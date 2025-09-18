
n=float(input())
if(n<3.0):
    print("under voltage")
elif(n>=3.0 and n<=3.3):
    print("normal voltage")
else:
    print("over voltage")