from math import *
def nt(n):
    if n<=1: return False
    for i in range(2, int(sqrt(n))+1):
        if(n%i==0): return False
    return True
def nn(a,n,nho):
    j=0
    for i in range(0,n):
       if(a[i]==nho):
           j=i
    return j
def dx(a,n):
    l,r=0,n-1
    while l<=r:
        if(a[l]!=a[r]): return False
        l+=1
        r-=1
    return True
def nhan(a,n):
    tich, mod=1,int(1e9+7)
    for i in range(0,n):
        tich*=a[i]%mod
        tich%=mod
    return tich
if __name__=='__main__':
    n=int(input())
    a = list(map(int,input().split()))
    m=max(a)
    ln= a.index(m)
    nho=min(a)
    tich=1
    print(m,ln)
    print(nho,nn(a,n,nho))
    b=[x for x in a if nt(x)]
    print(len(b))
    c=sorted(a)
    if c[0]<0 and c[1]<0:
        print(max(c[0]*c[1],c[n-1]*c[n-2]))
    else: print(c[n-1]*c[n-2])
    if dx(a,n): print('YES')
    else: print('NO')
    print(nhan(a,n))
