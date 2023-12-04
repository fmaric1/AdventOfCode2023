import re


brojac = 0

for i in range(1,216):
    game = input();
    gamei= game.split(":",1)[1]
    
    skupine = gamei.split(" |")
    dobitni = skupine[0].split(" ")
    moji = skupine [1].split(" ")
    pogodci = 0
    
    for x in dobitni:
        if x in moji and x.isnumeric():
            pogodci+=1
    if(pogodci>=1):
        brojac+= 2**(pogodci-1)

print(brojac)