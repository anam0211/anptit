def solve(a,n):
    d1,d2=0,0
    for i in range(0,n):
        if(a[i]==25):
            d1+=1
        elif(a[i]==50):
            if(d1==0): return False
            d2+=1
            d1-=1
        elif(a[i]==100):
            if(d1==0): return False
            if(d2==0 and d1<3): return False   
    return True
n=int(input())
a=list(map(int,input().split()))
if solve(a,n):
    print('YES')
else: print('NO ')

       

