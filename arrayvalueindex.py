val=[]
a=int(input())
val = list(map(int,input().split()))
for i in range(len(val)):
	print(val[i],end=" ")
	print(i)
