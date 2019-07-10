a=int(input())
f=1;  
if a<0:
   print("Invalid input");
else:
    while(a>0):
        f=f*a
        a=a-1
    print(f)
