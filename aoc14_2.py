from pathlib import Path
from itertools import combinations
import re

def count_rows(array):
    counter = 0
    for i in range(0,len(array)):
        x=(len(array)-1-i)*array[i].count("O")
        counter +=x
    return(counter)


def cycle (lines):
    ##North
    array = []
    for i in range(len(lines)):
        new_string = ''.join(string[i] for string in lines)
        array.append(new_string)


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

    # print("North")
    # for x in array:
    #     print(x)
    
    #West
    
    array3 =[]
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
        array3.append(string)
    
    # print("West")
    # for x in array3:
    #     print(x)

    #South
    array2 = []
    for i in range(len(array3)):
        new_string = ''.join(string[i] for string in array3)
        array2.append(new_string[::-1])

    array3 =[]
    for x in array2:
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
        array3.append(string+"#")
    
    array2=[]
    for i in range(len(array3)):
        new_string = ''.join(string[i] for string in array3)
        array2.insert(0,new_string)

    # print("south")
    # for x in array2:
    #     print(x)
    


#East
        
    array3 = []
    for x in array2:
        array3.append(x[::-1])

    array2 =[]
    for x in array3:
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
        array2.append(string)

    array3 = []
    for x in array2:
        array3.append(x[::-1])

    # print("East")
    # for x in array3:
    #     print(x)



    return array3

#####

file = Path(__file__).parent / "input.txt"
lines = file.read_text().split("\n")
for i in range(0,len(lines)):
    lines[i]='#'+lines[i]+'#'

string = "#"*len(lines[0])
lines.insert(0,string)
lines.append(string)



counter = 0
i = 0
map = []
map.append(lines)
array = lines
while(i< 1000000000):
    array = cycle(array)
    
    if array in map:
        period = i-map.index(array)+1
        index = (1000000000-i)%(period)
        array = map[i-period+index]
        
        map.append(array)
        break
    else:
        map.append(array)
        i+=1

counter = count_rows(array)

print(counter)