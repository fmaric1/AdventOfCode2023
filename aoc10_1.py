matrix = []
i = 0
j = 0
counter = 0

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
while(matrix[i][j]!='S'):
    if(matrix[i][j]== '|' and orientation == 2):
        i -= 1
    elif(matrix[i][j]== '|' and orientation == 0):
        i += 1

    elif(matrix[i][j]== '-' and orientation == 1):
        j -= 1
    elif(matrix[i][j]== '-' and orientation == 3):
        j += 1
        
    elif(matrix[i][j]== 'F' and orientation == 1):
        i += 1
        orientation = 0
    elif(matrix[i][j]== 'F' and orientation == 2):
        j += 1
        orientation = 3

    elif(matrix[i][j]== 'L' and orientation == 1):
        i -= 1
        orientation = 2
    elif(matrix[i][j]== 'L' and orientation == 0):
        j += 1
        orientation = 3
                
    elif(matrix[i][j]== 'J' and orientation == 0):
        j -= 1
        orientation = 1
    elif(matrix[i][j]== 'J' and orientation == 3):
        i -= 1
        orientation = 2
        
    elif(matrix[i][j]== '7' and orientation == 2):
        j -= 1
        orientation = 1
    elif(matrix[i][j]== '7' and orientation == 3):
        i += 1
        orientation = 0
    
    counter += 1
print((counter+1)/2)


        

    

