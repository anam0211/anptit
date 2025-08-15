def ucln(a,b):
    if b==0: return a
    return ucln(b,a%b)
def bcnn(a,b):
    return a*b//(ucln(a,b))
a,b=map(int,input().split())
print(ucln(a,b),bcnn(a,b))