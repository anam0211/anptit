def solve(a,n):
    ans=a[0]
    for i in range(1,n):
        if(a[i]>ans):
            print(a[i], end=' ')
            ans=a[i]
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    print(a[0],end=' ')
    solve(a,n)