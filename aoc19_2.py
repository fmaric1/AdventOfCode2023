from pathlib import Path
from itertools import combinations
import re
import copy


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
    
    if(len(a[1])>=2 and a[1][-1]=="A" and a[1][-2][-1]=="A"):
        print(a[1])
        a[1].pop()
        a[1].pop()
        a[1].append("A")
        print(a[1])
    map[a[0]]=a[1]

paths = [["in"]]
i = 0 
while(i < len(paths)):
    
    while(paths[i][-1] != "A" and paths[i][-1] != "R"):
        path = copy.deepcopy(paths[i])
        ifs = map[paths[i][-1]]
        for j in range(0,len(ifs)):
            z = []
            if (j==len(ifs)-1):
                z = ifs[j]
            else:
                z = (ifs[j].split(":"))[1]
            if( j == 0):
                paths[i].append(z)
            else:
                x = copy.deepcopy(path)
                x.append(z)
                paths.append(x)
        
    i+=1


print()
paths2= []
for x in paths:
    
    if(x[-1]=="A"):
        paths2.append(x)
paths = paths2




ranges = [list(([1, 4000] * 4)) for _ in range(len(paths))]

for i in range(0,len(paths)):
    x = paths[i]
    j = 0 
    while(j <len(x)-1):
        for y in map[x[j]][:-1]:
            z = y.split(":")
            if(z[1]==x[j+1]):
                dictionary = { "x>" : 0 , "x<" : 1 , "m>" : 2 , "m<" : 3 ,
              "a>" : 4 , "a<" : 5 , "s>" : 6 , "s<" : 7  }
                if(dictionary[z[0][0:2]]%2==0 and ranges[i][dictionary[z[0][0:2]]] < int(z[0][2:]) ):
                    ranges[i][dictionary[z[0][0:2]]] = int(z[0][2:])+1

                elif(dictionary[z[0][0:2]]%2==1 and ranges[i][dictionary[z[0][0:2]]] > int(z[0][2:]) ):
                    ranges[i][dictionary[z[0][0:2]]] = int(z[0][2:])-1
                
                break

            elif(z[1]!=x[j+1]):
                dictionary = { "x>" : 1 , "x<" : 0 , "m>" : 3 , "m<" : 2 ,
              "a>" : 5 , "a<" : 4 , "s>" : 7 , "s<" : 6  }
                if(dictionary[z[0][0:2]]%2==0 and ranges[i][dictionary[z[0][0:2]]] < int(z[0][2:]) ):
                    ranges[i][dictionary[z[0][0:2]]] = int(z[0][2:])

                elif(dictionary[z[0][0:2]]%2==1 and ranges[i][dictionary[z[0][0:2]]] > int(z[0][2:]) ):
                    ranges[i][dictionary[z[0][0:2]]] = int(z[0][2:])
                
            
        j+=1

sum = 0

    
#ranges = [list(t) for t in set(tuple(arr) for arr in ranges)]

#ranges = sorted(ranges, key=lambda x: tuple(x))
sum =0

for x in ranges:
    sum += (max(x[7]-x[6]+1,0))*max(x[5]-x[4]+1,0)*max(x[3]-x[2]+1,0)*max(x[1]-x[0]+1,0)
    


print(sum)
print("113550238315130")
#print(167409079868000- sum)
    