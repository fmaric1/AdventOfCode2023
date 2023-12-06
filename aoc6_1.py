import math

x = input()[11:]
time = x.split("   ")
time = [int(num.strip()) for num in time]

x = input()[11:]
distance = x.split("   ")

distance = [int(num.strip()) for num in distance]
sum = 1
solutions=[]
for i in range(0, len(time)):
    rjesenje = 0
    x1= math.ceil((time[i]+math.sqrt(time[i]*time[i]-4*1*distance[i]))/2)
    x2= math.floor((time[i]-math.sqrt(time[i]*time[i]-4*1*distance[i]))/2)

    for j in range(x2,x1):
        if((j*(time[i]-j))>distance[i]):
          
            rjesenje +=1
    
    if(rjesenje!=0):
        sum*=rjesenje

print(sum)