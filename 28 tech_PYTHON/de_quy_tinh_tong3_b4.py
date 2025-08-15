def tong4(n):
    if n==0: return 0
    if(n%2==0): return n+tong4(n-1)
    else: return -n+tong4(n-1)
if __name__=='__main__':
    n=int(input())
    print(tong4(n))