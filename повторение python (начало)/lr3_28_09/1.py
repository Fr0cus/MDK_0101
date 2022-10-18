y = float ( input ('Введите курс доллар в рублях : '))
 
dollars = []
for i in range (1, 21):
    dollars.append(round(i * y, 5))
 
x = 0
for i in range (0, 4):
    print (str(dollars[i+x:i+x+5]))
    x+=4