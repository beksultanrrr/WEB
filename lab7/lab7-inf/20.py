a=[]
c=int(input())
for i in range(c):
    b=int(input())
    a.append(b) 
cnt1=0
cnt2=0
cnt3=0
for i in range(c):
    if a[i]==0:
        cnt1+=1
    elif a[i]>0:
        cnt2+=1
    else:
        cnt3+=1
print(cnt1,cnt2,cnt3)
