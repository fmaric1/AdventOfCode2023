
import array
import re
red =[]
pocetak = 0
kraj = 0
brojac = 0
for i in range(0,142):
    red.insert(i,"..." + input() + "...")
for i in range(1,142):
    j = 3
    while j < 146:
        if(red[i][j]=="*"):
            x = []
            x.insert(0, red[i-1][(j-3):(j+5)])
            x.insert(1, red[i][(j-3):(j+5)])
            x.insert(2, red[i+1][(j-3):(j+5)])
            print(x[0])
            print(x[1])
            print(x[2])
            dijelovi = []
            for k in range(0,3):
                m = 0
                pocetak = 0
                kraj = 0
                
                while m < 8:
                    if(x[k][m].isdigit()):
                        pocetak = m
                        while(x[k][m].isdigit()):
                            m=m+1
                            if(m>7):
                                m=m-1
                                break
                        kraj = m
                    m = m+1
                    if(x[k][pocetak:kraj].isnumeric()):
                        print(x[k][pocetak:kraj])
                    if(( kraj == 3 or kraj == 4 or pocetak ==2 or pocetak ==3 or pocetak ==4) and x[k][pocetak:kraj].isnumeric()):
                        dijelovi.append(x[k][pocetak:kraj])
                        pocetak = m
                        kraj = m
                   
            print(dijelovi)
            if(len(dijelovi)==2):
                brojac += int(dijelovi[0])*int(dijelovi[1])
        j+=1
print(brojac)
