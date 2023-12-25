from pathlib import Path
from itertools import combinations
import re
from sympy import Point, Segment
from itertools import combinations

def shoelace(points):
    area = 0

    X = [point[0] for point in points] + [points[0][0]]
    Y = [point[1] for point in points] + [points[0][1]]

    for i in range(len(points)):
        area += X[i] * Y[i + 1] - Y[i] * X[i + 1]

    return abs(area) / 2

file = Path(__file__).parent / "input.txt"
lines2 = file.read_text().split("\n")


lines = []
for x in lines2:
    lines.append(x.split())

for i in range(0,len(lines)):
    
    if(lines[i][2][-2]=='0'):
        lines[i][0]="R"

    elif(lines[i][2][-2]=='1'):
        lines[i][0]="D"
    
    elif(lines[i][2][-2]=="2"):
        lines[i][0]="L"
    
    elif(lines[i][2][-2]=="3"):
        lines[i][0]="U"
    lines[i][1]=int(lines[i][2][2:-2],16)

coordinates = [[0,0]]
for x in lines:
    z = coordinates[len(coordinates)-1]
    x[1] = int(x[1])
    if(x[0]=='U'):
        coordinates.append([z[0], z[1]+x[1]])
    elif(x[0]=='D'):
        coordinates.append([z[0], z[1]-x[1]])
    elif(x[0]=='L'):
        coordinates.append([z[0]-x[1], z[1]])
    elif(x[0]=='R'):
        coordinates.append([z[0]+x[1], z[1]])

sum = abs(coordinates[len(coordinates)-1][0]) +abs(coordinates[len(coordinates)-1][1])

for x in lines:
    sum += int(x[1])

A = shoelace(coordinates)
b = sum
print(int(A+1-b/2+sum))
