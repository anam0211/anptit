from math import *
x1,y1,x2,y2=map(int,input().split())
x=pow(abs(x1-x2),2)
y=pow(abs(y1-y2),2)
res=sqrt(x+y)
print('%.2f' %res)