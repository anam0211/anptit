from math import *
def nt(n):
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return n>1
if __name__ == '__main__':
    n=int(input())
    dem=0
    while n!=0:
        if (nt(n%10)):
            dem+=1
        n//=10
    print(dem)    
        