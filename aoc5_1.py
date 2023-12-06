import re

x= input()
seeds = x.split(": ")[1].split()
seeds = [int(num) for num in seeds]
print(seeds) 
unos = "aa"
input()
for i in range(0,7):
    promijenjeno = [0]*20
    
    naziv = input()
    while(1):
        y = input()
        if(y ==''):
            break
        red = y.split()
        red = [int(num) for num in red]
        for j in range(0,20):
            if(seeds[j]>= red[1] and seeds[j]<=(red[1]+red[2]) and promijenjeno[j]==0):
                seeds[j]=red[0] + seeds[j] - red[1]
                promijenjeno[j]=1
print(min(seeds))
