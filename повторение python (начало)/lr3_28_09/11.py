from math import *
x = int(input("Введите факториал числа n:"))

for i in range(1, x+1):
    x = x/i
    if x == 1:
        print(i)
    else:
        continue
