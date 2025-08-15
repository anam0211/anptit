def solve(a,n):
    mini,maxi=1e9,-1e9
    for i in range (1,n-1):
        print(min(abs(a[i]-a[i-1]),abs(a[i+1]-a[i])), end=' ')
        print(max(abs(a[i]-a[0]),abs(a[i]-a[n-1])))
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    print(abs(a[1]-a[0]), end=' ')
    print(abs(a[n-1]-a[0]))
    solve(a,n)
    print(abs(a[n-1]-a[n-2]), end=' ')
    print(abs(a[n-1]-a[0]))