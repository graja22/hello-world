num1=int(input())
num2=num1
num3=0
num4=0
while(num1>0):
   num3=num1%10
   num1=num1//10
   num4+=num3*num3*num3
if num2==num4:
    print("yes")
else:
    print("no")
