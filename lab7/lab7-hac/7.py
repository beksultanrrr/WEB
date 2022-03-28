n = int(input())
arr = map(int, input().split())
max=-100000
max2=-10000
for i in range(n):
    if arr[i]>max:
        max=arr[i]
for i in range(n):
    if arr[i]<max:
        max2=arr[i]
print(max2)