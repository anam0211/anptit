from math import *

x,y=map(float,input().split())
z=pow(x,y)
f=floor(z)
if f==z: print(f)
else: print('%.2f' %z)
