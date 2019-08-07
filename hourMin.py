[h1, m1] = list(map(int, input().split()))
[h2, m2] = list(map(int, input().split()))

if(h1 > h2):
    if(m1 > m2):
        minute = m1-m2
    else:
        minute = (m1+60)-m2
        h1-=1
    hour = h1-h2
elif (h1 == h2 ):
    minute = abs(m1-m2)
    hour = h1
else:
    if(m2 > m1):
        minute = m2 - m1
    else:
        minute = (m2+60) - m1
        h2 -= 1
    hour = h2-h1

while(minute > 59):
    minute -= 60
    hour  += 1

print(hour, minute, end="")
    
