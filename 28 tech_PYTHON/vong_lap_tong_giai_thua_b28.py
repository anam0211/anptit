def tong(n):
    dex=1
    for i in range(2,n+1):
        dex*=i
    return dex    
if __name__ == '__main__':
    sum=0
    n=int(input())
    for i in range(1,n+1):
        sum+=tong(i)
    print(sum)    