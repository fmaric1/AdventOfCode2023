from pathlib import Path
from itertools import combinations
import re

file = Path(__file__).parent / "input.txt"
lines = file.read_text().split("\n")

counter = 0

for x in lines:
    
    if(x==''):
        break
    left, right = x.split(" ",1)
    
    right = right.split(',')
    right = [int(num) for num in right]
    index = [index for index, letter in enumerate(left) if letter == '?']
    
    inline_sum = sum(right)
    combs = list(combinations(index, inline_sum-x.count('#')))
    for y in combs:
        helpLine = x
        for i in y:
            helpLine = helpLine[:i]+'#'+helpLine[i+1:]
        helpLine = helpLine.replace("?",".")
        
        counts = []
        j = 0
        while(j < len(helpLine)):
            current_count = 0
            if helpLine[j] == '#':
                while(helpLine[j]=='#'):
                    current_count += 1
                    j+=1
                    if(j>=len(helpLine) or helpLine[j]!='#'):
                        break
                counts.append(current_count)
            
            j+=1
        if(right == counts):
            counter+=1  
print(counter)