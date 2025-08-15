from math import *
def pt(n):
    for i in range(2,int(sqrt(n))+1):
        while n%i==0:
            if(n%i==0): print(i,end=' ')
            n//=i
    if n!=1: print(n)
if __name__=='__main__':
    n=int(input())
    pt(n)