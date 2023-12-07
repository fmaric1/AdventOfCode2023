import re

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

rangirano = []
while(1):
    unos = input()
    if(unos ==''):
        break
    ruka = unos.split(" ")
    ruka.append(0)

    sortiran = ''.join(sorted(ruka[0]))
    # Five of a kind
    if re.search(r"([2-9TJQKA]).*?\1.*?\1.*?\1.*?\1", sortiran):
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