if __name__=='__main__':
    n=int(input())
    c,l=0,0
    for i in range(0,n):
        a=list(map(int,input().split()))
        for x in a:
            if x%2==0: c+=1
            else: l+=1
    if c<l:
        print('LE')
    elif c>l:
        print('CHAN')
    else: print('CHANLE')