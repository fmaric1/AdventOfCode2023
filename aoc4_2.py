import re


brojac = 0
brojtiketa = [1] * 215

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
    for j in range(0,pogodci):
        brojtiketa[i+j]+=brojtiketa[i-1]
for x in brojtiketa:
    brojac+=x
print(brojac)