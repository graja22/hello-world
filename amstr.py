a=int(input())
b=a
c=0
d=0
while(a>0):
   c=a%10
   a=a//10
   d+=c*c*c
if b==d:
    print("yes")
else:
    print("no")
