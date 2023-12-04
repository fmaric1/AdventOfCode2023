import re

boje = ["red", "green", "blue"]
limit = [12,13,14]

brojac = 0
for i in range(1,101):
    game = input();
    gamei= game.split(": ",1)[1]
    print(gamei)
    draws = gamei.split("; ")
    possible = True
    for draw in draws:
        possible = True
        colors = draw.split(", ")
        for x in colors:
            splited = x.split(" ")
            if(int(splited[0])>limit[boje.index(splited[1])]):
                possible= False
                break
        if(possible == False):
            break
    if(possible):
        brojac += i
print(brojac)