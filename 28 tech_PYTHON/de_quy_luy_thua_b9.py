mod =int(1e9+7)

def lt(a,b):
    if b==0: return 1
    n=lt(a,b//2)
    if(b%2==0): return n*n%mod
    return a%mod*n%mod*n%mod
a,b=map(int,input().split())
print(lt(a,b))