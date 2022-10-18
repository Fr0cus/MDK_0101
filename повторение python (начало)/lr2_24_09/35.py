#A
print("Введите координаты для задачи А")
x, y = int(input()), int(input())
if x <= -1 and y <= -2:
    print("Условие истинно")
else:
    print("Условие ложно")

#Б
print("Введите координаты для задачи Б")
y1, y2 = int(input()), int(input())
if y1 >= 1 or y2 <= -3:
    print("Условие истинно")
else:
    print("Условие ложно")