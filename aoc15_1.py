from pathlib import Path
from itertools import combinations
import re

file = Path(__file__).parent / "input.txt"
lines = file.read_text().split(",")
list = []
counter = 0
for x in lines:
    c = 0
    for i in range(0,len(x)):
        c  += ord(x[i])
        c = (c*17)%256
      
    counter += c
print(counter)