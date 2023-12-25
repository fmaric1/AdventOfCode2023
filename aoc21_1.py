from pathlib import Path


file = Path(__file__).parent / "input.txt"
lines = file.read_text().split("\n")

matrix = []
moves = [(1,0),(-1,0),(0,1),(0,-1) ]
i = 0 
j = 0
for k in range(0, len(lines)):
    if "S" in lines[k]:
        i = k
        j = lines[k].index('S')
        break

S = [(i,j)]
A = []

for k in range(0,64):
    for x in S:
        for y in moves:
            i = y[0]+x[0]
            j = y[1]+x[1]
            if(0<=i<len(lines) and 0<=j<len(lines[0]) and lines[i][j]!="#" and (i,j) not in A):
                A.append((i,j))
    S=A
    A=[]

print(len(S))