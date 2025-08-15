def dcs(n):
    if n==0: return 0
    return 1+dcs(n//10)
n=int(input())
if(n==0): print(1)

else: print(dcs(n)) 
