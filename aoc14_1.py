from pathlib import Path
from itertools import combinations
import re


#Ideja je da zapamtim pozicije "zidova", te prebrojim koliko je kamenja izmedu svaka dva zida u jednom redu, te onda ih pomjerim prema gornjem zidu,
# takoder sam na pocetku dodao zid oko cijelog inputa, kako ne bih morao gledati rubne slucajeve
file = Path(__file__).parent / "input.txt"
lines = file.read_text().split("\n")
for i in range(0,len(lines)):
    lines[i]='#'+lines[i]+'#'

string = "#"*len(lines[0])
lines.insert(0,string)
lines.append(string)

for x in lines:
    print(x)

array = []
for i in range(len(lines)):
    new_string = ''.join(string[i] for string in lines)
    array.append(new_string)

counter = 0

array2 =[]
for x in array:
    occurrences = [index for index, hash in enumerate(x) if hash == '#']
    if(0 not in occurrences):
        occurrences.insert(0,0)
    occurrences.append(len(x))
    c = []
    for i in range(0,len(occurrences)-1):
        num = x[occurrences[i]:occurrences[i+1]].count('O')
        c.append(num)
    string=""
    for i in range(0,len(occurrences)-1):
        string += "#"+"O"*c[i]+"."*(occurrences[i+1]-c[i]-occurrences[i]-1)
    array2.append(string+"#")

array = []
for i in range(len(array2)):
    new_string = ''.join(string[i] for string in array2)
    array.append(new_string)
for i in range(0,len(array)):
    x=(len(array)-1-i)*array[i].count("O")

    counter +=x


print(counter)
