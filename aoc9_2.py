import re
counter = 0
while(1):
    
    matrix = []
    x =input()
    if(x == ''):
        break
    row = x.split(' ')
    row = [int(num) for num in row]
    row.reverse()
    matrix.append(row)
    i = 0
    while(len(matrix[i])!=matrix[i].count(0)):
        i +=1
        matrix.append([])
        for j in range(0, len(matrix[i-1])-1):
            matrix[i].append(matrix[i-1][j+1]-matrix[i-1][j])

    for k in range(0,len(matrix)):
      
        index = len(matrix)-1-k
        if(index == len(matrix)-1):
            matrix[index].append(0)
        else:
            matrix[index].append(matrix[index][len(matrix[index])-1]+matrix[index+1][len(matrix[index])-1])
    counter+=matrix[0][len(matrix[0])-1]
print(counter)