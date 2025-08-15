def dautien(n):
    if n<10: return n
    return dautien(n//10)
n=int(input())
print(dautien(n))