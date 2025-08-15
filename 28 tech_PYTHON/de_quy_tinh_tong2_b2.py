def tong2(n):
    if n==1: return 1
    return n**3+tong2(n-1)
if __name__=='__main__':
    n=int(input())
    print(tong2(n))