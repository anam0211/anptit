def tcs(n):
    sum=0
    while(n!=0):
        sum+=n%10
        n//=10
    return sum
if __name__ == '__main__':
    n = int(input())
    while n>=10:
        n=tcs(n)
    print(n)