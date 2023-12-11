
i = 0
coordinates = []
counter = 0
map = []
row =[]
column = []
i = 0
while(1):
    x = input()
    if(x==''):
        break
    if(x.count('.') == len(x)):
        row.append(i)
    map.append(x)
    i+=1
combined_strings = [''.join(chars) for chars in zip(*map)]


i = 0
for x in combined_strings:
    
    if(len(x)==x.count('.')):
        column.append(i)
    i +=1



for i in range(0, len(map)):
    occurrences = [index for index, hash in enumerate(map[i]) if hash == '#']
    
    for y in occurrences:
       coordinates.append([i,y])
    i+=1
counter = 0
multiplier  = 2
for i in range(0,len(coordinates)-1):
    
    y = coordinates[i]
    for x in coordinates[i+1:]:
        a = min(y[0], x[0])
        b = max(y[0], x[0])
        c = min(y[1], x[1])
        d = max(y[1], x[1])

        counter += abs(x[1]-y[1]) +  abs(x[0]-y[0]) + len([x for x in row if a < x < b])*(multiplier-1) + len([x for x in column if c < x < d])*(multiplier-1)
        
print(counter)