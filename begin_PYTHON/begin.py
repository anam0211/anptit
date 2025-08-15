
""" begin
a=100
b=200
c=300
d='an'
e=100-50j
f=3.31324234234
 #print(a,b,c, sep='? ', end='/')
#day la chu thich """


"""
day la chu 
thich tren nhieu dong
"""

"""" in ra kieu du lieu, lam tron 
#print(type(d)) in  ra kieu du lieu cua bien
print(e)
print('%.2f' %f) #lam tron 2 chu so
g= nguyen hoai 
an
print(g) """


""" ep kieu:
s='12345' 
i=int(s)
print(i)
k=21424324221
st=str(k)
print(st) """


"""
 gan bien va swap
a,b,c=100,200,'ankuro'
print(a,b,c)

e=200
f=300
e,f=f,e
print(e,f)
 """


""" 
toan tu toan hoc
+ - * /
// chia nguyen
% chia du 
** luy thua
"""

""" toan tu logic
and toan tu va (20==20) and (1==1) true
or toan tu hoac or(10<20) or (20==50) true
not toan tu phu dinh not(20==20) false
"""


"""is so sanh hai doi tuong co nam trong cung o nho khong
a is b 
a is not b
"""

""" tim kiem tu trong xau
s='NGUYEN HOAI AN'
print('AN' in s)
print('PHUONG'not in s)
"""


""" nhap du lieu 
s=input('Nhap ten cua ban :')
print('in ra ten cua ban :', s)
a=input()
print(type(a)) #luon la kieu du lieu str

b=int(input('Nhap 1 so nguyen: ')) #ep kieu sang so int
print(type(b))
print(b)
"""

"""
s=input('Nhap 3 so : ')
a=s.split()  #a=[100,200,300]
x,y,z=map(int,a)
j,q,k=a
print(x+y+z) #cong cac so
print(j+q+k) #cong xau """

"""
x,y,z=map(int,input('Nhap 3 so').split())
print(x+y+z)
"""
#------------------------------------------------------
""" hamm
from math import *

print(sqrt(4)) #tra ve so thuc
isqrt #tra ve so nguyen
pow
ceil #lam tron len 2.2->3
floor #lam tron xuong 2.7-> 2
factorial #giai thua
gcd(a,b) #ucln
comb(n,k) #to hop chap k cua n

abs min max sum #ham co san
"""


"""
import math
print(help(math))
"""

#-------------------------------------------------
""" cau lenh if
a=8
if a>=10 and a%2==0:
    print('true')
elif a<10 and a%2==0:
    print('haft')
else: print('false')
"""
#--------------------------------------------
""" chuyen so ve ma ascii va ngươc lai
ord('A')   # 65
chr(65)    # 'A'
"""

#-----------------------------------------------
""" vong lap for va while
a=range(1,10,1)
for i in a:
    print(i,end=' ')


for i in range(51):
    print(i, end=' ') #in ra tu 0 den 50

for i in range(10,0,-1):
    print(i,end=' ') #giam tu 10 ve 1

print('\n')
n=10
s=0
for i in range(1,n+1):
    s+=i
print(s)

for i in range(1,7):
    print(i) #in ra so tu 1 den 7
    i+=100

for i in range(1,21):
    print(i, end=' ')
    if i%7==0:
        break
    print('cau lenh ben duoi break')

for i in range(1,10,3):
    print(i, end=' ')
"""


"""
a,b=10,20
while a<=b:
    print(a)
    a+=1



while True:
    n=int(input('Nhap n: '))
    if n>0: break

n=1234
dem=0
while n!=0:
    dem+=1
    n//=10
print(dem)    

n=1234
m=0
while n!=0:
    m=m*10+n%10
    n//=10
print(m)    

n=1234
print(len(str(n)))
"""

#----------------------------------------------
""" ham
def tong(a,b):
    res=a+b
    return res
print(tong(10,20))

def xinchao(name1,name2,name3):
    print('xin chao', name1,name2, name3)
xinchao('AN', 'Phương', 'My')

def change(n): #tam thoi
    n*=2

def infor(name,job='Xe om'):
    print(name,job)

def tonghieu(a,b):
    tong=a+b
    hieu=a-b
    return tong,hieu
#code de chay chuong trinh
if __name__ == '__main__':
    #code
    x,y= map(int, input().split())
    print(tong(x,y))
    a=100
    change(a) #chinh thuc
    print(a) #a khong thay doi gia tri
    xinchao('X','Y','Z') #posittional argument
    xinchao(name3='Teo', name2='Ty', name1='Nam')
    infor('28tech','Developer') #in ra 28tech Developer
    infor('Teo') #Default argument in ra teo Xe om
    t,h=tonghieu(10,20)
    print(t,h)
    print(tonghieu(10,20))
"""

"""
#----------------------------------------------------------------------

a=[1,2,3,4,5]
b=[1,2.3,'An','Chi']
s='NguyenAn'
a=list(s) #in ra N g u...
b=list(range(20))
print(a)
print(b)
print(len(a)) #do dai mang
print(a[5])
for i in range(0,len(a)):
    print(a[i],end=' ')
a.append(10) #them phan tu vao cuoi
a.insert(2,10) #them phan tu vao vi tri bat ki
a.pop(2) #xoa phan tu vi tri so 2
a.pop() #xoa phan tu o cuoi
a.remove(10) #xoa gia tri dau tien neu k co thang nao se bao loi
a.clear() #xoa moi phan tu
a+=b #noi 2 mang
a.conut(10) #dem so lan xuat hien
a.index(10) #tra ve chi so
a.reverse() #lat nguoc
a.sort() #O(Nlog(N))
print(max(a))
print(min(a))
print(sum(a))
b=sorted(a)#sap xep sang mang b moi
if 10 in a: #tim kiem 10 trong a O(N) 
a=[1,2,3]
b=a*2 #b= 123123
for x in a:
    print(x)
### change
a=[1,2,3,4]
b=a #a=b va id giong nhau thay doi a cung thay doi b
b=a.copy() #a va b khac nhau
b=a[:] #giong ham copy
### cat mang
#a[start,stop,step]
a=[10,20,30,40,50,60]
b=a[2 : 5 : 1] #30 40 50
b=a[ : 5] # tu 0 den 4
b=a[1 :] # tu 1 den cuoi
b=a[::-1] #lat nguoc mang a
a[2:5]=[1,2,3] #thay chi so 2 den 5 thanh 1 2 3
a[2:5]=[] #xoa
a[: 0]= [1,2,3] #chen vao dau
a[len(a) :]#chen vao cuoi

### lambda thay mang
func=lambda x,y,z : x+y+z
print(func(100,200,300))
print((lambda x,y,z : x+y+z)(100,200,300))
#thay doi ham
a=[1,2,3,4,5]
b=list(map(lambda x : x**2,a))
print(b) #1,4,9,16,25
#loc filter
a=[1,2,-3,-4,5]
b=list(filter(lambda x: x>0,a))
print(b) #1,2,5
b=list(filter(lambda x: x%2==0,a)) #tra ve true
# thay doi gia tri trong mang
def sum_digit(n):
    tong=0
    while n!=0:
        tong+=n%10
        n//=10
    return tong
a=[1,2,3,4,5]
b=[]
b=[x+3 for x in a]
print(b) #4 5 6 7 8


b=[sum_digit(x) for x in a]
print b

# loc cac gia tri trong list
def nt(n):
    for i in range(2, sqrt(n)+1):
        if n%i==0: return False
    return n>1

a=[1,-233,30,-4,99,-192,-13,123]
b=[x for x in a if x>=0]
print(b)

b=[x for x in a if(nt(x))]

# nhap mang

n=int(input())
a=list(map(int,input().split()))
"""
#-------------------------------------------------------------------
cnt=[0] *100000001#mang danh dau
#chi khi gan bien hay mang moi dung global
#vi du mang a= mang b, bien a= bien b


