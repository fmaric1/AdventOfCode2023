
import array
import re
red =[]
pocetak = 0
kraj = 0
brojac = 0
for i in range(0,143):
    red.insert(i,"." + input() + ".")

for i in range(1,142):
    j = 1
    while j < 142:
        if(red[i][j].isdigit()):
            pocetak = j
            while(red[i][j].isdigit()):
                j=j+1
            kraj = j
            for k in range(pocetak-1,kraj+1):
                if((red[i][k]!="." and not red[i][k].isdigit()) or (red[i-1][k]!="." and not red[i-1][k].isdigit()) or (red[i+1][k]!="." and not red[i+1][k].isdigit())):
                    brojac += int(red[i][pocetak:kraj])
                    print(int(red[i][pocetak:kraj]))
                    break
            j = kraj
        j+=1
print(brojac)
