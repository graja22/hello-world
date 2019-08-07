num=[]
c=int(input())
num = map(int,input().split())
d=sorted(num)
for i in range(len(d)):
        print (d[i],end=" ")
