n=int(input())
s=[]
for i in range(0,n):
    a=input().split(" ")
    a=[int(j) for j in a]
    s.append(a[0]+a[1])
for i in range(1,n+1):
    print(f'Case #{i}: {s[i-1]}')