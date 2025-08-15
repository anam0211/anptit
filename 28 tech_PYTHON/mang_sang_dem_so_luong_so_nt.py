from math import *
prime = [1] *(10**6+1)
def sang():
    prime[0],prime[1]=0,0
    for i in range(2,isqrt(10**6)+1):
        if prime[i]==1:
            for j in range(i*i,10**6+1,i):
                prime[j]=0
if __name__=='__main__':
    t=int(input())
    f=[0] * (10**6+1)
    f[0],f[1]=0,0
    sang()
    for i in range(2,10**6+1):
        f[i]=f[i-1]+prime[i]
    for i in range(0,t):
        n=int(input())
        print(f[n])