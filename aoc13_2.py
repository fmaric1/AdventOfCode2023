from pathlib import Path
from itertools import combinations
import copy


def find_matching_pairs(array_of_strings):
    matching_pairs = []

    # Iterate through each pair of strings
    for i in range(len(array_of_strings)):
        for j in range(i + 1, len(array_of_strings)):
            # Check if the strings at indexes i and j are the same
            if array_of_strings[i] == array_of_strings[j]:
                matching_pairs.append((i, j))
    print(matching_pairs)
    return matching_pairs

def find_one_char_difference(array_of_strings):
    result = []

    # Iterate through each pair of strings
    for i in range(len(array_of_strings)):
        for j in range(i + 1, len(array_of_strings)):
            # Check if the strings at indexes i and j have only one character difference
            diff_count = sum(1 for a, b in zip(array_of_strings[i], array_of_strings[j]) if a != b)
            if diff_count == 1:
                result.append((i, j))

    return result

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
#############################################
def check_mirror2(array):
    pairs = find_one_char_difference(array)
    value = check_mirror(array)
    
    array2 = copy.deepcopy(array)
    for x in pairs:
        
        array = copy.deepcopy(array2)
        array[x[0]]=array[x[1]]   
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
                if(mirror and  value != 100*n):
                    return 100*n    
    array3 = []
    for i in range(len(array2[0])):
        new_string = ''.join(string[i] for string in array2)
        array3.append(new_string)
        
    array2 = copy.deepcopy(array3)
    pairs = find_one_char_difference(array2)
    for x in pairs:
        
        array3 = copy.deepcopy(array2) 
        array3[x[0]]=array3[x[1]]   
      
        for i in range(0,len(array3)-1):
          if(array3[i]==array3[i+1]):
                n=i+1
                j=i+1
                mirror = True
                while(i>=0 and j<len(array3)):
                    if(array3[i]!=array3[j]):
                        mirror=False
                        break
                    i-=1
                    j+=1
                if(mirror and value != n):
                    return n    
    return 0




counter = 0
array =[]
x  = input()
while(x!=''):
    if(x==''):
        break
    while(x != ''):
            array.append(x)
            x =input()    
    counter += check_mirror2(array)
    
    array=[]
    x=input()
print(counter)