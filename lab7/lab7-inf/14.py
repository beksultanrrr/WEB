import math
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    c=math.sqrt(i)
    if i%c==0:
        print(i)