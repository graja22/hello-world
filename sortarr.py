val=[]
a=int(input())
val = map(int,input().split())
c=sorted(val)
for i in range(len(c)):
        print (c[i],end=" ")
