import re
jedan = 0
dva = 0
brojac = 0
x = ""
while(1):
    jedan = "0"
    dva = "0"
    y = input()
    if(y=="kraj"):
        break
    x = y.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e").replace("zero", "z0o")
    for char in x:
        if char.isdigit():
            jedan = char
            break
    for char in x[::-1]:
        if char.isdigit():
            dva = char
            break
    broj = jedan + dva
    print(broj)
    brojac += int(broj)


print(brojac)
        
