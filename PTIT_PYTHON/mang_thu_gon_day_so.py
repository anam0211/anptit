if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    while(i<len(a)-1):
        if (a[i]+a[i+1])%2==0:
            a.pop(i)
            a.pop(i)
            i=max(i-1,0)
        else: i+=1

    
    print(len(a))
