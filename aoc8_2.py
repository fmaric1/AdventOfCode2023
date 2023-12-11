import re
from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

niz = input()
x = input()
mapa  = {}
trenutni = []
while(1):
    x = input()
    if(x ==''):
        break
    mapa[x[0:3]]= [x[7:10], x[12:15]]
    if(x[2]=="A"):
        trenutni.append( x[0:3])

i = 0
brojac =0
numbers = []
print(trenutni)
for j in range(0,len(trenutni)):
    i = 0
    brojac =0
    while(1):
        if(niz[i] == "L"):
            trenutni[j] = mapa[trenutni[j]][0]
        elif(niz[i] == "R"):
            trenutni[j] = mapa[trenutni[j]][1]
            
        if(trenutni[j][2]== "Z"):
           numbers.append(brojac+1)
           break
    
        i+=1 
        brojac +=1
        if(i == len(niz)):
            i =0
print(numbers)
lcm_result = reduce(lcm, numbers)  
print( lcm_result)