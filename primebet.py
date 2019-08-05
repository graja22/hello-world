[a,b]=list(map(int,input().split()))
flag = False;
for num in range(a, b ):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:
           if (flag == True) :
               print(end=" ")
           print(num, end="")
           flag = True

