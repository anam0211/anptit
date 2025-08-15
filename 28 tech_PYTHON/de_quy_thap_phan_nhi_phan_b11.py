def np(n):
    if n==0:
        return
    np(n//2)
    print(n%2, end='')
  
n=int(input())
if n==0: print('0')
else: np(n)