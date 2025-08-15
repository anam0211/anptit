def gcd(a,b):
    while b!=0:
        a,b=b,a%b

    return a
def ucln(a,b):
    return (a*b)//gcd(a,b)
if __name__=='__main__':
    print(gcd(18,15))
    print(ucln(18,15))
    from math import *
    print(comb(10,2))