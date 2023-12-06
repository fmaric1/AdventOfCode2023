import re


x= input()
seeds = x.split(": ")[1].split()
seeds = [int(num) for num in seeds]
print(seeds) 
unos = "aa"
input()
mape=[]

for i in range(0,7):
    mape.append([])
    
    naziv = input()
    while(1):
        y = input()
        if(y ==''):
            break
        red = y.split()
        red = [int(num) for num in red]
        mape[i].append(red)
        mape[i] = sorted(mape[i], key=lambda x: x[1])

range2 = []
range3 =[]
for i in range(0,len(seeds),2):
    range2.append([seeds[i],seeds[i]+seeds[i+1]])

for i in range(0,7):
    range1=sorted(range2, key=lambda x: x[0])
    range2=[]
    decoder = mape[i]

    for x in range1:
        for y in decoder:
            range_start = y[1]
            range_end = y[1] + y[2]
            if range_start < x[1] and x[0] < range_end:
                intersection_start = max(range_start, x[0])
                intersection_end = min(range_end, x[1])
                range2.append([y[0]+intersection_start-y[1],  y[0]+intersection_end-y[1]])
                if(x[0]<intersection_start):
                    x[1]=intersection_start
                else:
                    x[0]=intersection_end
               
        
        if(x[0]!=x[1]):
            range2.append([x[0],x[1]])
    for z in range2:
        range3.append(z)
   
range3= sorted(range3, key=lambda x: x[0])
print(range3)
print(range3[0])


