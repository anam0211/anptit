def tong5(n):
    if n==1: return 1
    return 1/n + tong5(n-1)
n=int(input())
print('%.3f' %tong5(n))