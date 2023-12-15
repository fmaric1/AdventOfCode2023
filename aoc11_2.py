from pathlib import Path

file = Path(__file__).parent / "input.txt"
map = file.read_text().split("\n")

def empty_space(map):
    i = 0
    list = []
    for x in map:
        if(len(x)==x.count('.')):
            list.append(i)
        i +=1
    return list

coordinates = []

row =empty_space(map)
mapT = [''.join(chars) for chars in zip(*map)]
column = empty_space(mapT)

for i in range(0, len(map)):
    occurrences = [index for index, hash in enumerate(map[i]) if hash == '#']
    
    for y in occurrences:
       coordinates.append([i,y])
    i+=1

counter = 0
multiplier  = 1000000
for i in range(0,len(coordinates)-1):
    
    y = coordinates[i]
    for x in coordinates[i+1:]:
        a = min(y[0], x[0])
        b = max(y[0], x[0])
        c = min(y[1], x[1])
        d = max(y[1], x[1])

        counter += abs(x[1]-y[1]) +  abs(x[0]-y[0]) + len([x for x in row if a < x < b])*(multiplier-1) + len([x for x in column if c < x < d])*(multiplier-1)
        
print(counter)