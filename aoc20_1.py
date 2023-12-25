from pathlib import Path
from itertools import combinations
file = Path(__file__).parent / "input.txt"
lines = file.read_text().split("\n")


broadcaster = []
ff = {} #flip-flop
con = {}



for x in lines:
    y = x.split(" -> ")
    if(y[0][0]=="%"):
        ff[y[0][1:]]= [False, y[1].split(", ")]
    elif(y[0][0]=="&"):
        con[y[0][1:]]= [{}, y[1].split(", ")]
    else:
        broadcaster = y[1].split(", ")

for x in con.keys():
    for y in ff.keys():
        if(x in ff[y][1]):
            con[x][0][y]=0
    for y in con.keys():
        if(x in con[y][1]):
            con[x][0][y]=0

#print(ff)
#print(con)

pulseCounter = [0,0]
sendList = []

for i in range(0,1000):
    #print()
    
    pulseCounter[0]+=1
    for x in broadcaster:
        pulseCounter[0]+=1
        sendList.append([x,0,"broadcaster"])
            

    while(len(sendList)!=0):
        #print(sendList)
        x = sendList.pop(0)
       
        if(x[0] in ff):   #ako je x flip flop
            if(x[1]==0): #ako je primljeni signal low signal
                ff[x[0]][0]= not ff[x[0]][0] #upali ili ugasi flip flop
                for y in ff[x[0]][1]:  #za cijelu listu kojoj salje taj flip flop
                    sendList.append([y,int(ff[x[0]][0]),x[0]]) #posalji signal kontra
                    pulseCounter[int(ff[x[0]][0])]+=1
                    
        
        
        elif(x[0] in con): #ako je con
            
            for y in con[x[0]][1]: #za cijelu listu kojoj se salje
            
                #print((con[x[0]][0]))
                con[x[0]][0].update({x[2]:x[1]})
                
                if(list((con[x[0]][0].values())).count(1) == len(list((con[x[0]][0].values())))):
                    pulseCounter[0]+=1    
                    sendList.append([y,0,x[0]])
                else:
                    pulseCounter[1]+=1    
                    sendList.append([y,1,x[0]])
       # print(pulseCounter)




print(pulseCounter)
print(pulseCounter[0]*pulseCounter[1])


