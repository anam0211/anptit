"""phai return de tra ve gia tri 
check(2468) → số cuối là 8 (chẵn) → gọi check(246)
check(246) → 6 → check(24)
check(24) → 4 → check(2)
check(2) → 2 → check(0)
check(0) → return True"""
#code:
def check(n):
    if n==0: return True
    if (n%10)%2!=0: return False
    return check(n//10) #phai return
n=int(input())
if(check(n)): print('YES')
else: print('NO')
########################################################
