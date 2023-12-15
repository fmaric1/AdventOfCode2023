from pathlib import Path
from itertools import combinations
import re



def check_mirror(array):
    for i in range(0,len(array)-1):
          if(array[i]==array[i+1]):
                n=i+1
                j=i+1
                mirror = True
                while(i>=0 and j<len(array)):
                    if(array[i]!=array[j]):
                        mirror=False
                        break
                    i-=1
                    j+=1
                if(mirror):
                    return 100*n

    array2 = []
    for i in range(len(array[0])):
        new_string = ''.join(string[i] for string in array)
        array2.append(new_string)
    for i in range(0,len(array2)-1):
        if(array2[i]==array2[i+1]):
            n=i+1
            j=i+1
            mirror = True
            while(i>=0 and j<len(array2)):
                if(array2[i]!=array2[j]):
                    mirror=False                        
                    break
                i-=1
                j+=1
            if(mirror):
                return n
             
counter = 0
array =[]
x  = input()
while(x!=''):
    if(x==''):
        break
    while(x != ''):
            array.append(x)
            x =input()    
    counter+=check_mirror(array)
    
    array=[]
    x=input()
print(counter)