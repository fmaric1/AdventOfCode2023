from pathlib import Path
from itertools import combinations
import re

file = Path(__file__).parent / "input.txt"
lines = file.read_text().split(",")
list = []

hashmap = []
for i in range(0,256):
    hashmap.append([])
counter = 0
for x in lines:
    c = 0
    if "=" in x:
        for i in range(0,len(x)-2):
            c  += ord(x[i])
            c = (c*17)%256
    else:
        for i in range(0,len(x)-1):
            c  += ord(x[i])
            c = (c*17)%256

    if(x[-1]=='-'):
        if any(pair[0] == x[0:-1] for pair in hashmap[c]):
            hashmap[c].pop(next((i for i, pair in enumerate(hashmap[c]) if pair[0] == x[0:-1]), -1))
    else:
        if any(pair[0] == x[0:-2] for pair in hashmap[c]):
            hashmap[c][next((i for i, pair in enumerate(hashmap[c]) if pair[0] == x[0:-2]), -1)][1] = x[-1]
        else:
            hashmap[c].append([x[0:-2],x[-1]])

for i in range(0, 256):
    for j in range(0, len(hashmap[i])):
        counter += (i+1)*(j+1)*int(hashmap[i][j][1])
print(counter)
