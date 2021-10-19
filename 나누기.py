a=input().split(" ")
a=[int(i) for i in a]
print((a[0]+a[1])%a[2])
print(((a[0]%a[2])+(a[1]%a[2]))%a[2])
print((a[0]*a[1])%a[2])
print(((a[0]%a[2])*(a[1]%a[2]))%a[2])