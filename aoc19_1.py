from pathlib import Path
from itertools import combinations
import re



def splitIf(string):
    array = string.split("{")
    array2 = array[1][0:-1]
    ifs = array2.split(",")
    return [array[0], ifs]
    

file = Path(__file__).parent / "input.txt"
lines = file.read_text().split("\n")

map = {}
parts = []

empty_string_index = lines.index('')

# Splitting the array at the empty string index
first_part = lines[:empty_string_index]
second_part = lines[empty_string_index + 1:]

for x in first_part:
    a = splitIf(x)
    map[a[0]]=a[1]

for x in second_part:
    parts.append(x[1:-1].split(","))
    
i = 0
place = ["in"]*len(parts)

while(i<len(parts)):
    part = parts[i]
    x=int(part[0][2:])
    m=int(part[1][2:])
    a=int(part[2][2:])
    s=int(part[3][2:])
    while(place[i]!= 'A' and place[i]!='R'):
        ifs = map[place[i]]
        for j in range(0,len(ifs)):
            if(j == len(ifs)-1):
                place[i]=ifs[j]
                break
            else:
                z = ifs[j].split(":")
                if(eval(z[0])):
                    place[i]=z[1]
                    break
               
    i+=1
sum  = 0    
for i in range(0, len(place)):
    if(place[i]=="A"):
        sum += int(parts[i][0][2:]) + int(parts[i][1][2:]) + int(parts[i][2][2:]) +int(parts[i][3][2:])
print(sum)