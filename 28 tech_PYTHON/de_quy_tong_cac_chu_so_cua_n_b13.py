def tcs(n):
    if(n<10): return n
    return n%10+tcs(n//10)
n=int(input())
print(tcs(n))