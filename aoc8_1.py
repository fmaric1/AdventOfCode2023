import re

niz = input()
x = input()
mapa  = {}
while(1):
    x = input()
    if(x ==''):
        break
    mapa[x[0:3]]= [x[7:10], x[12:15]]
i = 0
brojac =0
trenutni = "AAA"
while(1):
    if(trenutni == "ZZZ"):
        break
    if(niz[i] == "L"):
        trenutni = mapa[trenutni][0]
    elif(niz[i] == "R"):
        trenutni = mapa[trenutni][1]
    i+=1
    brojac +=1
    if(i == len(niz)):
        i =0
print( brojac)