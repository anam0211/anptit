def tang(a,n):
    for i in range(1,n):
        if a[i]<=a[i-1]: return False
    return True
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    if tang(a,n):
        print('YES')
    else: print('NO')