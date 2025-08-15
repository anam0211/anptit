t=int(input())
sum=0
for i in map(int,input().split()):
    if(i%2==0): sum+=i
    t-=1
    if(t==-1): break

print(sum)        