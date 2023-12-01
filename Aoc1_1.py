import re
jedan = 0
dva = 0
brojac = 0
x = ""
while(1):
    jedan = "0"
    dva = "0"
    x = input()
    if(x=="kraj"):
        break
    for char in x:
        if char.isdigit():
            jedan = char
            break
    for char in x[::-1]:
        if char.isdigit():
            dva = char
            break
    broj = jedan + dva
    brojac += int(broj)


print(brojac)
        
