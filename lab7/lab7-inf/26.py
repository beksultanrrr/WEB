a=int(input())
l=[]
for i in range(a):
    b=int(input())
    l.append(b)
e=[]
for i in range(a):
    if l[i]%2==0:
        e.append(l[i])
print(*e)