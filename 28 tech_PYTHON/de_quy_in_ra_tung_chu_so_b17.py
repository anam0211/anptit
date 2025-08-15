def lr(n):
    if n<10: 
        print(n,end=' ')
        return
    lr(n//10)
    print(n%10, end=' ')
def rl(n):
    print(n%10,end=' ')
    if n<10: return
    rl(n//10)
   
n=int(input())
lr(n)
print('\n')
rl(n)