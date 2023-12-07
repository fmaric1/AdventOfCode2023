import re

card_values = {
    'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13
}

rangirano = []
while(1):
    unos = input()
    if(unos ==''):
        break
    ruka = unos.split(" ")
    ruka.append(0)

    
    sortiran = ''.join(sorted(ruka[0]))
    pomocni = sortiran.replace("J", "")
    counter = [0] *13
    if (len(pomocni) != 5):
        for i in range(0,len(pomocni)):
            counter[card_values[pomocni[i]]-1] +=1
        max_element = 0
        max_index = None
        for i in range(len(counter)):
            if counter[i] >= max_element:
                max_element = counter[i]
                max_index = i
        

        key= [key for key, value in card_values.items() if value == max_index+1]
        pomocna2 = ruka[0].replace("J", key[0])

        sortiran = ''.join(sorted(pomocna2))
        
    # Five of a kind
    if (len(set(sortiran)) == 1):
        ruka[2] = 7

    # Four of a kind
    elif re.search(r"([2-9TJQKA]).*?\1.*?\1.*?\1", sortiran):
        ruka[2] = 6

    # Full house
    elif (len(set(sortiran)) == 2):
        ruka[2] = 5

    # Three of a kind
    elif re.search(r"([2-9TJQKA]).*?\1.*?\1", sortiran):
        ruka[2] = 4

    # Two pair
    elif re.search(r'(\w)\1.*(\w)\2', sortiran):
        ruka[2] = 3

    # One pair
    elif (len(set(sortiran)) == 4):
        ruka[2] = 2

    # High card
    else:
        ruka[2] = 1


    rangirano.append(ruka)
sortirano = sorted(rangirano, key=lambda x: (x[2], card_values[x[0][0]],  card_values[x[0][1]],  card_values[x[0][2]],  card_values[x[0][3]],  card_values[x[0][4]]))
brojac = 0
for i in range(0,len(sortirano)):
    brojac += (i+1)*int(sortirano[i][1])


print(brojac)