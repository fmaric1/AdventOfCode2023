import math

x = input()[11:]
time = int(x.replace(" ", ""))


x = input()[11:]
distance = int(x.replace(" ", ""))
sum = 1


x1= math.ceil((time +math.sqrt(time *time -4*1*distance ))/2)
x2= math.floor((time -math.sqrt(time *time -4*1*distance ))/2)
rjesenje = x1-2-x2-2
for j in range(x1-2,x1):
    if((j*(time-j))>distance):      
        rjesenje +=1
    
for j in range(x2,x2+2):
    if((j*(time-j))>distance):      
        rjesenje +=1

print(rjesenje)