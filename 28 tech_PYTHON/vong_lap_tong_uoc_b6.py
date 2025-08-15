from math import *
def tonguoc(n):
    sum=0
    for i in range(1,int(sqrt(n)+1)):
        if n%i==0:
            sum+=i
            if(i!=n//i): sum+=n//i
    return sum

if __name__ == '__main__':
    a=int(input())
    print(tonguoc(a))