def check(n):
    if n==0: return True
    if (n%10)%2!=0: return False
    return check(n//10)
n=int(input())
if(check(n)): print('YES')
else: print('NO')