def hex(n):
    if n==0:
        return
    hex(n//16)
    if n%16>9:
        print(chr(ord('A')+n%16-10),end='')
    else:
        print(n%16, end='')
n=int(input())
if n==0: print('0')
else: hex(n)