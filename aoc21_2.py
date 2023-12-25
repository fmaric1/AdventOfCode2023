from pathlib import Path


file = Path(__file__).parent / "input.txt"
lines = file.read_text().split("\n")

size = (len(lines))

moves = [(1,0),(-1,0),(0,1),(0,-1) ]
i = 0 
j = 0
for k in range(0, len(lines)):
    if "S" in lines[k]:
        i = k
        j = lines[k].index('S')
        break

counter =0
hash =0 
for k in range(0,size):
    for l in range(0,size):
        if(k%2==0 and l%2==0 and lines[k][l]!="#"):
            counter+=1
        if(lines[k][l]=="#"):
            hash+=1
print(counter)
print(hash)
S = [(i,j)]
A = []
niz = []
m = i
n = j
second_elements =[]
for k in range(0,6):
    for x in S:
        for y in moves:
            i = y[0]+x[0]
            j = y[1]+x[1]
            if((((i+size)%size== m and j==n) or (i == m and (j+size)%size==n) )and i!=j and [i,j] not in second_elements):
                niz.append((k,[i,j]))
                second_elements = [t[1] for t in niz]
            if( lines[(i+size)%size][(j+size)%size]!="#" and (i,j) not in A):
                A.append((i,j))
    S=A
    A=[]
print(niz)
print(len(S))