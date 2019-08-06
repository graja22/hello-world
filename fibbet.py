a= int(input())
n1 = 1
n2 = 1
 
print(n1, n2, end=" ")
 
for i in range(2,a):
	next = n1 + n2
	print(next, end=" ")
 
	n1 = n2
	n2 = next
