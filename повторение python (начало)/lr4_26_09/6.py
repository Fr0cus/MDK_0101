a=[13,10,20,40,35,34,10,10,20,40,35,30,10,12,20,40,35,38,10,10,20,40,35,30,10,10,20,40,35,30,10,20,40,35,30,10,10,20,40,35,30,10]
for i in range(len(a)):
    if a[i] % 2 ==0:
        print("Чётные элемент:", a[i])
    

for i in range(len(a)):
    if a[i] % 10 == 0:
        print("Оканчивается на ноль:", a[i])
