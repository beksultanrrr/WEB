a=int(input())
b=int(input())
if b%a==0:
    print(0)
elif b%a!=0:
    print(b-(a*(b//a)))