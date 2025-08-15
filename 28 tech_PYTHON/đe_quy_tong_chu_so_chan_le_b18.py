suml=0
def tc(n):
    global suml
    if(n<10 and n%2==0):
        suml+=n%10
        return 
    if((n%10)%2==0):
        suml+=n%10
    tc(n//10)
    return suml
def tl(n):
    if n==0: return 0
    m=n%10
    if(m%2!=0): return m+tl(n//10)
    return tl(n//10)
n=int(input())
print(tc(n))
print(tl(n))