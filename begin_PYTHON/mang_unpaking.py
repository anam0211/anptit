a=[1,2,3]
x,y,z=a
print(x,y,z)#1,2,3
data=['CR7','BU','CU','MESSI']
name,tat,_,_=data
print(name,tat) #CR7,BU
s='CR7' 
a,b,c=s
print(a,b,c)#C,R,7  
a,b,c=range(0,5,2)
print(a,b,c) #0,2,4
a=[['A',65],['B',66],['C',67]]
for kt,ma in a:
    print(kt,ma)

a=[1,2,3,45,32,42,424,1,2]
x,y,*z=a
print(x)#1
print(y)#2
print(z)#....