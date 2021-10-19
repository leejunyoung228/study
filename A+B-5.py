s=[]
while True:
    a=input().split(" ")
    a=[int(i) for i in a]
    if a[0]+a[1]==0:break
    s.append(a[0]+a[1])
for i in s:
    print(i)