if __name__=='__main__':
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    ok=0
    for i in range(0,n):
        if a[i]==x:
            a.pop(i)
            ok=1
            break
    if ok==0: print('NOT FOUND')
    else: 
        for x in a:
            print(x, end=' ')
