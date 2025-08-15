def tt(n):
    if n==1: return 0
    x,y,z=1e9,1e9,1e9
    if n%2==0: x=1+tt(n//2)
    if n%3==0: y=1+tt(n//3)
    if n>1: z=1+tt(n-1)
    return min(min(x,y),z)
n=int(input())
print(tt(n))