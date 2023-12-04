import re

boje = ["red", "green", "blue"]


brojac = 0
for i in range(1,101):
    limit = [0,0,0]
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
                limit[boje.index(splited[1])]=int(splited[0])

    brojac += limit[0]*limit[1]*limit[2]
print(brojac)