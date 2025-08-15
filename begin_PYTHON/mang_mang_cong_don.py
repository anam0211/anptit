n=int(input())
a=list(map(int,input().split()))
f=[0] * n
f[0]=a[0]
for i in range(0,n):
    f[i]=f[i-1]+a[i]
l,r=3,5
if l==0: print(f[r])
print(f[r]-f[l-1])
