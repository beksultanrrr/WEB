a=int(input())
l=[]
for i in range(a):
    b=int(input())
    l.append(b)

cnt=0
for i in range(1,a):
    if (l[i]>0 and l[i-1]>0) or (l[i]<0 and l[i-1]<0):
        cnt+=1

if cnt==1:
    print("YES")
else:
    print("NO")