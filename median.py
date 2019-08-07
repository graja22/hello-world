import statistics
val=[]
a=int(input())
val = map(int,input().split())
num=statistics.median(val)
print(num)
