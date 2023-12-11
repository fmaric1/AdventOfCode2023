import copy

matrix = []
i = 0
j = 0
counter = 0

def shoelace(points):
    area = 0

    X = [point[0] for point in points] + [points[0][0]]
    Y = [point[1] for point in points] + [points[0][1]]

    for i in range(len(points)):
        area += X[i] * Y[i + 1] - Y[i] * X[i + 1]

    return abs(area) / 2

while(1):
    x = input()
    if(x == ''):
        break
    matrix.append(x)
    if('S' in x):
        i = counter
        j = x.find('S')
    
    counter +=1

orientation = 0
valid = False
V = [[i,j]]
if( (matrix[i-1][j] =='F' or matrix[i-1][j] =='|' or matrix[i-1][j] =='7') and not valid):
    
    i = i -1
    orientation = 2
    valid = True
elif( (matrix[i][j+1] =='-' or matrix[i][j+1] =='7' or matrix[i][j+1] =='J') and not valid):
    j = j + 1
    orientation = 3
    valid = True
elif( (matrix[i][j-1] =='-' or matrix[i][j-1] =='F' or matrix[i][j-1] =='L') and not valid):
    j = j - 1
    orientation = 1
    valid = True
elif( (matrix[i+1][j] =='L' or matrix[i+1][j] =='|' or matrix[i+1][j] =='J') and not valid):
    i = i -1
    orientation = 2
    valid = True

counter =0 
matrix2 = copy.deepcopy(matrix) 

b = 1
while(matrix[i][j]!='S'):
    if(matrix[i][j]== '|' and orientation == 2):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        i -= 1
        
    elif(matrix[i][j]== '|' and orientation == 0):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        i += 1

    elif(matrix[i][j]== '-' and orientation == 1):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        j -= 1

    elif(matrix[i][j]== '-' and orientation == 3):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        j += 1
        
    elif(matrix[i][j]== 'F' and orientation == 1):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        V.append([i,j])
        i += 1
        orientation = 0
        

    elif(matrix[i][j]== 'F' and orientation == 2):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        V.append([i,j])
        j += 1
        orientation = 3

    elif(matrix[i][j]== 'L' and orientation == 1):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        V.append([i,j])
        i -= 1
        orientation = 2
        

    elif(matrix[i][j]== 'L' and orientation == 0):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        V.append([i,j])
        j += 1
        orientation = 3
        
                
    elif(matrix[i][j]== 'J' and orientation == 0):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        V.append([i,j])
        j -= 1
        orientation = 1

    elif(matrix[i][j]== 'J' and orientation == 3):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        V.append([i,j])
        i -= 1
        orientation = 2

    elif(matrix[i][j]== '7' and orientation == 2):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        V.append([i,j])
        j -= 1
        orientation = 1

    elif(matrix[i][j]== '7' and orientation == 3):
        matrix[i]=matrix[i][:j]+'O'+matrix[i][j+1:]
        V.append([i,j])
        i += 1
        orientation = 0
    b+=1

A = shoelace(V)

print(int(A+1 -b/2))

