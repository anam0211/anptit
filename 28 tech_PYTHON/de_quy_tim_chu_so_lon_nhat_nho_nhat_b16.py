def ln(n):
    if n<10: return n 
    return max(n%10,ln(n//10))
def nn(n):
    if n<10: return n
    return min(n%10,nn(n//10))

n=int(input())

print(ln(n),nn(n))
